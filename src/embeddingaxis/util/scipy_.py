from scipy.spatial.distance import cosine

from embeddingaxis.types import SampleSimilarity
from embeddingaxis.util.openai_ import get_embedding

def get_distance(text1: str, text2: str) -> float:
    """Return the cosine distance between the embeddings of two texts.
    
    The theoretical range of the return value is [0, 2].
    The practical range of the return value with OpenAI embeddings is [0, 1].

    Lower values indicate more similar texts.
    Higher values indicate more dissimilar texts.
    """
    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)
    distance = cosine(embedding1, embedding2)
    return float(distance)

def get_similarity(text1: str, text2: str) -> float:
    """Return the cosine similarity between the embeddings of two texts.
    
    The theoretical range of the return value is [-1, 1].
    The practical range of the return value with OpenAI embeddings is [0, 1].

    Lower values indicate more dissimilar texts.
    Higher values indicate more similar texts.
    """
    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)
    similarity = 1 - cosine(embedding1, embedding2)
    return float(similarity)

def get_similar(sample: str, ref1: str, ref2: str) -> SampleSimilarity:
    """Return the more similar of two texts to a sample text."""
    similarity1 = get_similarity(sample, ref1)
    similarity2 = get_similarity(sample, ref2)
    nearest = ref1 if similarity1 > similarity2 else ref2
    separation = abs(similarity1 - similarity2)

    return SampleSimilarity(
        sample=sample,
        ref1=ref1,
        ref2=ref2,
        similarity1=similarity1,
        similarity2=similarity2,
        nearest=nearest,
        separation=separation,
    )