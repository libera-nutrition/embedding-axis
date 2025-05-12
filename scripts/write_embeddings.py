"""
This script ensures that all specified strings have their embeddings stored in the output JSON file.

Specifically, it:
- Skips strings that already have embeddings.
- Fetches missing embeddings.
- Writes the updated embeddings to the output file.
"""

import json

from embeddingaxis.config import PERSISTENT_CACHE_EMBEDDINGS, PERSISTENT_CACHE_EMBEDDINGS_STRINGS, PERSISTENT_CACHE_EMBEDDINGS_PATH
from embeddingaxis.util.openai_ import get_embedding

print(f"Ensuring embeddings for {len(PERSISTENT_CACHE_EMBEDDINGS_STRINGS)} strings in {PERSISTENT_CACHE_EMBEDDINGS_PATH}.")
for s in PERSISTENT_CACHE_EMBEDDINGS_STRINGS:
    if s in PERSISTENT_CACHE_EMBEDDINGS:
        print(f"Skipped preexisting embedding for {s!r}.")
        continue
    emb = get_embedding(s)
    PERSISTENT_CACHE_EMBEDDINGS[s] = emb

PERSISTENT_CACHE_EMBEDDINGS = {s: PERSISTENT_CACHE_EMBEDDINGS[s] for s in sorted(PERSISTENT_CACHE_EMBEDDINGS_STRINGS)}
PERSISTENT_CACHE_EMBEDDINGS_PATH.write_text(json.dumps(PERSISTENT_CACHE_EMBEDDINGS, indent=2))
print(f"Ensured embeddings for {len(PERSISTENT_CACHE_EMBEDDINGS_STRINGS)} strings. Wrote to {PERSISTENT_CACHE_EMBEDDINGS_PATH}.")
