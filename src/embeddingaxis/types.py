from typing import Required, TypedDict

class SampleSimilarity(TypedDict):
    """A dictionary representing a sample and its similarity to two references."""
    nearest: Required[str | None]
    separation: Required[float]
