import json
from pathlib import Path

import diskcache

from embeddingaxis.util.dotenv_ import load_dotenv

load_dotenv()

CWD: Path = Path.cwd()
PACKAGE_PATH: Path = Path(__file__).parent
PACKAGE_NAME: str = PACKAGE_PATH.name

_GiB: int = 1024**3
DISKCACHE: diskcache.FanoutCache = diskcache.FanoutCache(directory=str(PACKAGE_PATH / ".diskcache"), shards=8, timeout=10, size_limit=5 * _GiB)
PERSISTENT_CACHE_EMBEDDINGS_STRINGS: set[str] = {
    "",
    "weight loss",
    "weight gain",
    "fat loss",
    "fat gain",
    "muscle loss",
    "muscle gain",
    "healthy",
    "unhealthy",
}
PERSISTENT_CACHE_EMBEDDINGS_PATH: Path = PACKAGE_PATH / "data" / "embeddings.json"
PERSISTENT_CACHE_EMBEDDINGS: dict[str, list[float]] = json.loads(PERSISTENT_CACHE_EMBEDDINGS_PATH.read_text())