"""OpenRouter AI client for image analysis.

Uses OPENROUTER_API_KEY and OPENROUTER_MODEL from environment.
Sends a base64-encoded image and returns structured analysis JSON.

Usage:
    from agents.metadata.ai_client import analyze_with_ai
"""

from __future__ import annotations

import base64
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv(".secrets/cline-db.env")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

DEFAULT_MODEL = "deepseek/deepseek-chat-v3-0324"

SYSTEM_PROMPT = """Analyze this image in the context of the original World Trade Center complex (pre-2001).

Return a JSON object with the following fields:
- asset_type: one of [photo, document, blueprint, video, audio, unknown]
- asset_type_confidence: 0-100 integer
- description: brief description of visible content
- tower: One World Trade Center, Two World Trade Center, or Unknown
- floor: floor number or Unknown
- area: specific area name (Plaza, Lobby, Observation Deck, Concourse, etc.) or Unknown
- estimated_year: YYYY or Unknown
- tags: comma-separated keywords
- confidence_score: 0-100 overall analysis confidence

IMPORTANT: Do not invent details. Use 'Unknown' when uncertain.
Base all observations on visible evidence only."""


def _get_mime_type(image_path: str) -> str:
    """Map file extension to MIME type."""
    ext = os.path.splitext(image_path)[1].lower()
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }.get(ext, "image/jpeg")


def analyze_with_ai(image_path: str) -> dict:
    """Send image to OpenRouter for structured analysis.

    Returns a dict with asset_type, asset_type_confidence, description,
    tags, tower, floor, area, estimated_year, confidence_score, model.
    """
    model = os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL)

    # Read and encode image
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    mime_type = _get_mime_type(image_path)
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")
    data_uri = f"data:{mime_type};base64,{image_b64}"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": SYSTEM_PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {"url": data_uri},
                    },
                ],
            }
        ],
        "response_format": {"type": "json_object"},
        "max_tokens": 500,
    }

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY', '')}",
        "Content-Type": "application/json",
    }

    resp = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=60)
    resp.raise_for_status()

    result = resp.json()
    content = result["choices"][0]["message"]["content"]
    parsed = json.loads(content)

    return {
        "asset_type": parsed.get("asset_type", "unknown"),
        "asset_type_confidence": int(parsed.get("asset_type_confidence", 25)),
        "description": parsed.get("description", "No description available"),
        "tags": parsed.get("tags", ""),
        "tower": parsed.get("tower", "Unknown"),
        "floor": parsed.get("floor", "Unknown"),
        "area": parsed.get("area", "Unknown"),
        "estimated_year": parsed.get("estimated_year", "Unknown"),
        "confidence_score": int(parsed.get("confidence_score", 50)),
        "model": model,
    }