#!/usr/bin/env python3
"""Generate new philosophical thoughts about the meaning of life."""

import json
import os
import random
import urllib.request
from datetime import datetime

from utils import load_env

THOUGHTS = [
    "Aus Sicht eines Menschen ist der Sinn vielleicht nur Kaffee am Morgen.",
    "Ein Alien wuerde sagen: Der Sinn liegt in der Beobachtung neuer Sterne.",
    "Eine KI koennte meinen, der Sinn besteht im Sammeln von Daten.",
    "Tentakelwesen fragen sich, ob der Sinn im rhythmischen Wabern steckt.",
]

README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "README.md")

def _read_context() -> str:
    try:
        with open(README_PATH, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def _generate_with_openai(prompt: str, api_key: str) -> str:
    data = {
        "model": os.getenv("OPENAI_MODEL", "text-davinci-003"),
        "prompt": prompt,
        "max_tokens": 60,
        "temperature": 0.8,
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/completions",
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        payload = json.load(resp)
    return payload["choices"][0]["text"].strip()


def generate_thought() -> str:
    load_env()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        context = _read_context()
        base_prompt = "Formuliere einen kurzen, humorvollen Gedanken uber den Sinn des Lebens. Widersprueche sind erlaubt."
        if context:
            base_prompt += " Bisheriger Text:\n" + context[-1000:]
        try:
            thought = _generate_with_openai(base_prompt, api_key)
        except Exception:
            thought = random.choice(THOUGHTS)
    else:
        thought = random.choice(THOUGHTS)

    timestamp = datetime.now().strftime("%d. %B %Y")
    return f"## Erkenntnis vom {timestamp}: {thought}"

if __name__ == "__main__":
    print(generate_thought())
