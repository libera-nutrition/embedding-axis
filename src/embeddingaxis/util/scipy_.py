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

def get_similar(sample: str, ref1: str, ref2: str, *, debias: bool = True) -> SampleSimilarity:
    """Return the more similar of two references texts to the sample text.
    
    If `debias` is True, the similarity is debiased by subtracting the similarity of the empty string to the reference texts.
    """
    similarity1 = get_similarity(sample, ref1)
    similarity2 = get_similarity(sample, ref2)

    if debias:
        similarity1 -= get_similarity("", ref1)
        similarity2 -= get_similarity("", ref2)

    nearest = {
        similarity1 == similarity2: None, 
        similarity1 > similarity2: ref1,
        similarity1 < similarity2: ref2,
    }[True]
    separation = similarity1 - similarity2

    return SampleSimilarity(
        nearest=nearest,
        separation=separation,
    )