from typing import Required, TypedDict

class SampleSimilarity(TypedDict):
    """A dictionary representing a sample and its similarity to two references."""
    sample: Required[str]
    ref1: Required[str]
    ref2: Required[str]
    similarity1: Required[float]
    similarity2: Required[float]
    nearest: Required[str]
    separation: Required[float]
