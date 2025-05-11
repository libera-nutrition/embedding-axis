import openai

from embeddingaxis.util.dotenv_ import load_dotenv

load_dotenv()

def get_embedding(text: str, **kwargs) -> list[float]:
    """Return the embedding vector for the given text."""
    response = openai.embeddings.create(input=text, model="text-embedding-3-large", **kwargs)
    return response.data[0].embedding
