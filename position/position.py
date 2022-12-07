from dataclasses import dataclass

__all__ = ("OpenPositions")


@dataclass(eq=False, repr=True)
class OpenPositions:
    type: str
    contract: str
