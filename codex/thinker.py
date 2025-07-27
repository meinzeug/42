#!/usr/bin/env python3
import random
from datetime import datetime

THOUGHTS = [
    "Aus Sicht eines Menschen ist der Sinn vielleicht nur Kaffee am Morgen.",
    "Ein Alien wuerde sagen: Der Sinn liegt in der Beobachtung neuer Sterne.",
    "Eine KI koennte meinen, der Sinn besteht im Sammeln von Daten.",
    "Tentakelwesen fragen sich, ob der Sinn im rhythmischen Wabern steckt."
]

def generate_thought():
    thought = random.choice(THOUGHTS)
    timestamp = datetime.now().strftime("%d. %B %Y")
    return f"## Erkenntnis vom {timestamp}: {thought}"

if __name__ == "__main__":
    print(generate_thought())
