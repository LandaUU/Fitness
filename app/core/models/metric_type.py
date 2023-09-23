from dataclasses import dataclass


@dataclass
class MetricType:
    id: int
    type: str
    description: str
