"""
This script ensures that all specified strings have their embeddings stored in the output JSON file.

Specifically, it:
- Loads existing embeddings from the data file.
- Skips strings that already have embeddings.
- Fetches and appends missing embeddings.
- Outputs progress and summary information to the console.
"""

import json
from pathlib import Path

from embeddingaxis.util.openai_ import get_embedding

STRINGS = [
    "weight loss",
    "weight gain",
    "fat loss",
    "fat gain",
    "muscle loss",
    "muscle gain",
    "healthy",
    "unhealthy"
]

OUTPUT_PATH = Path(__file__).parent.parent / 'src/embeddingaxis/data/embeddings.json'

if OUTPUT_PATH.exists():
    print(f"Loading preexisting embeddings from {OUTPUT_PATH}.")
    embeddings = json.loads(OUTPUT_PATH.read_text())
    print(f"Loaded {len(embeddings)} preexisting embeddings.")
else:
    print(f"The embeddings output path {OUTPUT_PATH} does not exist.")
    embeddings = {}

print(f"Ensuring embeddings for {len(STRINGS)} strings in {OUTPUT_PATH}.")
for s in STRINGS:
    if s in embeddings:
        print(f"Skipped preexisting embedding for {s!r}.")
        continue
    emb = get_embedding(s)
    embeddings[s] = emb
    print(f"Retrieved embedding for {s!r}.")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

embeddings = {s: embeddings[s] for s in STRINGS}
OUTPUT_PATH.write_text(json.dumps(embeddings, indent=2))
print(f"Ensured embeddings for {len(STRINGS)} strings. Wrote to {OUTPUT_PATH}.")
