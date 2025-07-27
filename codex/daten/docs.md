# Dokumentation

## Technologien
- **Python** fuer die Skripte `thinker.py` und `updater.py`.
- **Bash** fuer `scheduler.sh` (Cron-kompatibel).
- **Markdown** fuer alle Textdateien.
- Optional: **OpenAI API** fuer Textgenerierung.

## Module und Dateien
### thinker.py
- Implementiert die Logik zur Generierung neuer philosophischer Beitraege.
- Nutzt ggf. ein LLM ueber eine API.
- Gibt den generierten Text an `updater.py` weiter.

### updater.py
- Ergaenzt die README.md um den neuen Beitrag.
- Fuegt Zeitstempel hinzu und haelt den humorvollen Stil bei.
- Optional: Append in `logs/history.log`.

### scheduler.sh
- Ein Shell-Skript, das Thinker und Updater periodisch ausfuehrt.
- Kann per Cronjob eingebunden werden.

## Ablauf
1. Scheduler ruft `thinker.py` auf.
2. thinker.py generiert eine neue Erkenntnis.
3. updater.py schreibt die Erkenntnis in die README.md und das Log.
4. Prozess wiederholt sich.

## API-Anbindung
- API-Schluessel in `.env` ablegen.
- Zugriff ueber ein einfaches Python-Modul in `thinker.py`.
