import openai
import json
from pathlib import Path

from embeddingaxis.util.dotenv_ import load_dotenv

load_dotenv()

_EMBEDDINGS_FILE_CACHE = json.loads((Path(__file__).parent.parent / "data" / "embeddings.json").read_text())

def _get_embedding(text: str) -> list[float]:
    """Return the embedding vector for the given text."""
    response = openai.embeddings.create(input=text, model="text-embedding-3-large")
    print(f"Got embedding for {text!r}.")
    return response.data[0].embedding


def get_cached_embedding(text: str) -> list[float]:
    """Return the embedding vector for the given text, using cache if available."""
    try:
        return _EMBEDDINGS_FILE_CACHE[text]
    except KeyError:
        pass

    return _get_embedding(text)
