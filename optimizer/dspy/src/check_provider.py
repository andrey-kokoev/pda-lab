#!/usr/bin/env python3
"""Minimal provider/auth check for DSPy/OpenAI-compatible endpoints."""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv
import requests

ROOT = Path(__file__).resolve().parents[3]
ENV_PATH = ROOT / ".env"
load_dotenv(ENV_PATH, override=False)


def configured_api_base() -> str:
    return os.getenv("OPENAI_API_BASE") or os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1"


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = configured_api_base()
    model = os.getenv("DSPY_MODEL")

    if not api_key:
        raise SystemExit("Missing OPENAI_API_KEY in .env or environment")
    if not model:
        raise SystemExit("Missing DSPY_MODEL in .env or environment")

    if model.startswith("openai/"):
        model = model.split("/", 1)[1]

    url = base_url.rstrip("/") + "/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Reply with exactly: ok"}],
        "temperature": 1,
        "max_tokens": 8,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
    print(f"POST {url}")
    print(f"HTTP {response.status_code}")

    try:
        body = response.json()
    except Exception:
        print(response.text)
        raise SystemExit(1)

    print(json.dumps(body, indent=2)[:4000])

    if response.status_code >= 400:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
