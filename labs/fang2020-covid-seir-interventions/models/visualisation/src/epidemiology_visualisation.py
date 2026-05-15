# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Desktop-compatible epidemiology visualisation model."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import AcceptedSignalProfile, BioSignal, SignalSpec
from biosim.signals import unwrap_payload


def _payload(signal: BioSignal | Any) -> Any:
    if signal is None:
        return None
    try:
        value = unwrap_payload(signal)
    except Exception:
        value = getattr(signal, "value", signal)
    if isinstance(value, Mapping) and set(value) == {"payload"}:
        return value["payload"]
    return value


def _finite_number(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number or number in (float("inf"), float("-inf")):
        return None
    return number


def _label(name: str, labels: Mapping[str, str]) -> str:
    return str(labels.get(name) or name).replace("_", " ")


def _schema_for(source: Mapping[str, Any], name: str) -> dict[str, str]:
    schemas = source.get("schemas")
    if isinstance(schemas, Mapping):
        schema = schemas.get(name)
        if isinstance(schema, Mapping) and schema:
            return {str(key): str(value) for key, value in schema.items()}
    return {"payload": "json"}


class EpidemiologyVisualisationModel(BioModule):
    """Render Q/A, timeseries, and burden-summary visuals from core outputs."""

    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        sources: list[dict[str, Any]],
        caveat: str = "Values are native SBML quantities; the bundled source model was executed without rewriting equations.",
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = lab_title
        self.question = question
        self.sources = sources
        self.caveat = caveat
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: dict[str, list[dict[str, float]]] = {str(src["alias"]): [] for src in sources}
        self._labels: dict[str, dict[str, str]] = {str(src["alias"]): {} for src in sources}
        self._summaries: dict[str, dict[str, Any]] = {}
        self._time = 0.0

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self.reset()

    def reset(self) -> None:
        self._inputs = {}
        self._history = {str(src["alias"]): [] for src in self.sources}
        self._labels = {str(src["alias"]): {} for src in self.sources}
        self._summaries = {}
        self._time = 0.0

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        for source in self.sources:
            alias = str(source["alias"])
            for name in ("state", "summary", "species_labels"):
                schema = _schema_for(source, name)
                specs[f"{alias}_{name}"] = SignalSpec.record(
                    schema=schema,
                    accepted_profiles=(AcceptedSignalProfile(signal_type="record", schema=schema),),
                    description=f"{alias} {name} feed for epidemiology visualisation.",
                )
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        self._time = float(end)
        for source in self.sources:
            alias = str(source["alias"])
            labels = _payload(self._inputs.get(f"{alias}_species_labels"))
            if isinstance(labels, Mapping):
                self._labels[alias] = {str(k): str(v) for k, v in labels.items()}
            summary = _payload(self._inputs.get(f"{alias}_summary"))
            if isinstance(summary, Mapping):
                self._summaries[alias] = dict(summary)
            state = _payload(self._inputs.get(f"{alias}_state"))
            if isinstance(state, Mapping):
                row = {"t": self._time}
                for key, value in state.items():
                    number = _finite_number(value)
                    if number is not None:
                        row[str(key)] = number
                if len(row) > 1:
                    self._history.setdefault(alias, []).append(row)

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> list[dict[str, Any]]:
        visuals: list[dict[str, Any]] = []
        for source in self.sources:
            alias = str(source["alias"])
            history = self._history.get(alias) or []
            if not history:
                continue
            labels = self._labels.get(alias, {})
            series = self._series(history, labels)
            if series:
                visuals.append({
                    "render": "timeseries",
                    "title": "Observed epidemiology dynamics",
                    "data": {"series": series},
                    "description": "Selected state variables from the bundled source model.",
                })
            bars = self._burden_items(history, labels)
            if bars:
                visuals.append({
                    "render": "bar",
                    "title": "Latest burden snapshot",
                    "data": {"items": bars},
                    "description": "Latest finite values for selected epidemiology observables.",
                })
            visuals.append(self._answer_table(alias, history, labels))
        return [item for item in visuals if self._has_renderable_data(item)]

    def _series(self, history: list[dict[str, float]], labels: Mapping[str, str]) -> list[dict[str, Any]]:
        keys = [key for key in history[-1] if key != "t"][:8]
        series = []
        for key in keys:
            points = [[row["t"], row[key]] for row in history if key in row]
            if points:
                series.append({"name": _label(key, labels), "points": points})
        return series

    def _burden_items(self, history: list[dict[str, float]], labels: Mapping[str, str]) -> list[dict[str, Any]]:
        latest = history[-1]
        items = [
            {"label": _label(key, labels), "value": float(value)}
            for key, value in latest.items()
            if key != "t" and _finite_number(value) is not None
        ]
        items.sort(key=lambda item: abs(item["value"]), reverse=True)
        return items[:8]

    def _answer_table(self, alias: str, history: list[dict[str, float]], labels: Mapping[str, str]) -> dict[str, Any]:
        first = history[0]
        latest = history[-1]
        changes: list[tuple[str, float]] = []
        for key, value in latest.items():
            if key == "t":
                continue
            changes.append((key, abs(float(value) - float(first.get(key, value)))))
        changes.sort(key=lambda item: item[1], reverse=True)
        dominant = changes[0][0] if changes else ""
        dominant_label = _label(dominant, labels) if dominant else "No changing observable"
        peak_key, peak_value = max(
            ((key, abs(float(value))) for key, value in latest.items() if key != "t"),
            key=lambda item: item[1],
            default=("", 0.0),
        )
        if changes and changes[0][1] > 0:
            observed = f"{dominant_label} changed most over the simulated window."
        else:
            observed = "The selected observables were near steady over the simulated window."
        evidence = f"Peak latest magnitude: {_label(peak_key, labels)} = {peak_value:.6g}" if peak_key else "Finite baseline state was produced."
        return {
            "render": "table",
            "title": "Scientific answer",
            "data": {
                "columns": ["Item", "Value"],
                "rows": [
                    ["Scientific question", self.question],
                    ["Observed answer", observed],
                    ["Evidence", evidence],
                    ["Dominant module", dominant_label],
                    ["Caveat", self.caveat],
                ],
            },
        }

    def _has_renderable_data(self, visual: Mapping[str, Any]) -> bool:
        data = visual.get("data")
        if not isinstance(data, Mapping):
            return False
        render = visual.get("render")
        if render == "bar":
            return bool(data.get("items")) and "categories" not in data and "values" not in data
        if render == "timeseries":
            return bool(data.get("series")) and all(item.get("points") for item in data.get("series", []))
        if render == "scatter":
            return bool(data.get("points"))
        if render == "table":
            rows = data.get("rows")
            prompts = [row[0] for row in rows or [] if isinstance(row, list) and row]
            return bool(rows) and "Observed answer" in prompts and "Question" not in prompts
        return False
