from typing import Required, TypedDict

class SampleSimilarity(TypedDict):
    """A dictionary representing a sample and its similarity to two references."""
    nearest: Required[str | None]
    separation: Required[float]

class SampleScaledSimilarity(SampleSimilarity):
    """A dictionary representing a sample, its similarity, and scaled similarity to two references."""
    scaled_separation: Required[float]