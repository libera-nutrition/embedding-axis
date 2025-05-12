import openai
import json
from pathlib import Path

from embeddingaxis.config import PERSISTENT_CACHE_EMBEDDINGS
from embeddingaxis.util.dotenv_ import load_dotenv

load_dotenv()

def get_embedding(text: str) -> list[float]:
    """Return the embedding vector for the given text."""
    response = openai.embeddings.create(input=text, model="text-embedding-3-large")
    print(f"Got embedding for {text!r}.")
    return response.data[0].embedding


def get_cached_embedding(text: str) -> list[float]:
    """Return the embedding vector for the given text, using cache if available."""
    try:
        return PERSISTENT_CACHE_EMBEDDINGS[text]
    except KeyError:
        pass

    return get_embedding(text)
