"""Export the OpenAPI schema and build a static docs site into ./site."""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from main import app  # noqa: E402

OUT = ROOT / "site"

OUT.mkdir(exist_ok=True)
(OUT / "openapi.json").write_text(json.dumps(app.openapi(), indent=2))
shutil.copy(ROOT / "docs_static" / "index.html", OUT / "index.html")
(OUT / ".nojekyll").touch()
print(f"Built docs in {OUT}")
