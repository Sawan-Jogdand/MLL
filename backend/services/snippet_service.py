import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SNIPPETS_DIR = (BASE_DIR / "snippets").resolve()
SNIPPET_NAME_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,64}$")


def list_snippets():
    files = sorted(SNIPPETS_DIR.glob("*.txt"))
    return [p.stem for p in files]


def get_snippet(name: str):
    safe_name = name.strip().lower()
    if not SNIPPET_NAME_PATTERN.fullmatch(safe_name):
        return None

    path = (SNIPPETS_DIR / f"{safe_name}.txt").resolve()
    if path.parent != SNIPPETS_DIR or not path.is_file():
        return None
    return path.read_text(encoding="utf-8")
