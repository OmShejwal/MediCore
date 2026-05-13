from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BACKEND_ROOT = Path(__file__).resolve().parent
LEGACY_BACKEND_DIR = BACKEND_ROOT.parent / "Hackathon" / "backend"
LEGACY_MAIN_FILE = LEGACY_BACKEND_DIR / "main.py"

# Load root backend env first so Render and local runs can use backend/.env.
load_dotenv(dotenv_path=BACKEND_ROOT / ".env", override=False)


def _load_legacy_app():
    spec = importlib.util.spec_from_file_location("medicore_legacy_backend_main", LEGACY_MAIN_FILE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load backend implementation from {LEGACY_MAIN_FILE}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.app


app = _load_legacy_app()


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8002))
    uvicorn.run(app, host="0.0.0.0", port=port)