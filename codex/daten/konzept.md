# Technisches Konzept

## Projektziel
Eine autonome KI-Instanz soll fortlaufend ueber den Sinn des Lebens philosophieren und diese Gedanken
selbst in der README.md festhalten. Die KI soll unterschiedliche Perspektiven (Mensch, Alien, KI,
Tentakelwesen etc.) einnehmen und sich dabei gelegentlich widersprechen.

## Hauptfunktionen
1. **Thinker** (`codex/thinker.py`)
   - Liest den aktuellen Inhalt der README.md.
   - Generiert neuen philosophischen Text mit Zeitstempel.
   - Gibt den Text zur Weiterverarbeitung an den Updater.
2. **Updater** (`codex/updater.py`)
   - Fuegt den generierten Text unten in die README.md ein.
   - Schreibt den Beitrag optional zusaetzlich in `logs/history.log`.
3. **Scheduler** (`codex/scheduler.sh`)
   - Ruft Thinker und Updater in regelmaessigen Abstaenden auf (z.B. per Cron).

## Dateistruktur
```
ki-sinn-des-lebens/
├── codex/
│   ├── thinker.py         # KI-Philosophielogik
│   ├── updater.py         # README-Aktualisierung
│   └── scheduler.sh       # Zeitsteuerung
├── logs/
│   └── history.log        # Archiv aller Erkenntnisse
├── README.md              # Zentraler Tempel der Gedanken
└── .env                   # Umgebungsvariablen und API-Keys
```

## Komponenten
- **KI/LLM-Anbindung:** Fuer die Textgenerierung kann ein LLM (z.B. OpenAI) genutzt werden.
- **Logging:** Alle Eintraege koennen in `logs/history.log` archiviert werden.
- **Konfiguration:** `.env` enthaelt API-Schluessel und Einstellungen fuer Scheduler und Updater.

## Besonderheiten
- Humorvoller Ton und gelegentliche Widersprueche sind erwuenscht.
- Zeitstempel in lesbarer Form (z.B. `27. Juli 2025`).
- Modularer Aufbau, so dass einzelne Komponenten leicht angepasst werden koennen.
