

# 1) Neues Projekt in PyCharm anlegen

1. PyCharm → **New Project**
2. **Pure Python** wählen → Projektname z. B. `rsv-desktop`
3. **New Virtualenv** aktiv lassen → Create

---

# 2) Pakete installieren

In PyCharm unten **Terminal** öffnen (im Projektordner) und:

```bash
pip install --upgrade pip
pip install pywebview pyinstaller
```

> Hinweis Windows: PyWebView nutzt den **Edge WebView2**. Auf 99 % der Systeme ist der Runtime schon drauf. Falls beim Start eine Meldung kommt, den „WebView2 Runtime (Evergreen)“ installieren (kleiner Installer von Microsoft).

---

# 3) Datei `app.py` anlegen (minimal, robust)

Im Projekt eine neue Datei **`app.py`** erstellen:

```python
import webview

URL = "https://rsv-saal.de"

def main():
    # Fenster erstellen
    window = webview.create_window(
        title="RSV Saal",
        url=URL,
        width=1280,
        height=800,
        resizable=True,
        fullscreen=False
    )
    # Startet das native WebView (Windows: Edge WebView2)
    webview.start()

if __name__ == "__main__":
    main()
```

Start-Test in PyCharm: ▶️ **Run ‘app’** – es sollte sich sofort ein Fenster öffnen und deine Seite laden.

---

# 4) Icon vorbereiten (optional, aber schön)

* Lege eine **`icon.ico`** (mind. **256×256 px**) ins Projektverzeichnis.
* Das Icon wird für die EXE genutzt.

---

# 5) Portable .exe bauen (ohne Konsolenfenster)

Im PyCharm-Terminal:

```bash
pyinstaller --onefile --noconsole --name "RSV Saal" --icon=icon.ico app.py
```

Ergebnis:

```
dist/
  RSV Saal.exe   ← deine portable Datei
```

Doppelklick → lädt `rsv-saal.de` im eigenen Fenster.
Die Datei ist portabel (keine Installation), entpackt sich nur temporär im Hintergrund.

---

## Optionales Feintuning

### A) Start maximiert

```python
window = webview.create_window("RSV Saal", URL, width=1280, height=800)
# direkt maximieren geht via JS/Events nicht immer 100% – meist reicht eine größere Startgröße
```

### B) Single-Instance (nur eine App-Instanz zulassen)

Ein einfacher Ansatz mit Dateisperre (zusätzl. Paket `filelock`):

```bash
pip install filelock
```

```python
from filelock import FileLock, Timeout
import sys, os
lock = FileLock(os.path.join(os.path.expanduser("~"), ".rsv_saal.lock"))
try:
    lock.acquire(timeout=0.1)
except Timeout:
    sys.exit(0)
```

→ Vor `main()` aufrufen.

### C) Fehlermeldung, falls offline

Du kannst einfach „laden lassen“, oder minimal prüfen – z. B. mit `requests` (optional):

```bash
pip install requests
```

```python
import requests
try:
    requests.head(URL, timeout=3)
except Exception:
    URL = "about:blank"  # oder lokale Info-Seite
```

---

## macOS / Linux später

* **macOS**: gleiche `app.py`, auf einem Mac bauen:

  ```bash
  pip install pywebview pyinstaller
  pyinstaller --onefile --windowed --name "RSV Saal" --icon=icon.icns app.py
  ```

  → erzeugt eine `.app` (bzw. in `dist/`).
* **Linux**: analog, optional als AppImage über zusätzliche Tools.

---

## Troubleshooting (kurz)

* **„No WebView2 runtime found“**: Den **Microsoft Edge WebView2 Runtime** installieren (Evergreen). Danach klappt’s.
* **EXE startet, zeigt kurz nichts und schließt**: Meist weil mit `--console` gebaut wurde und Fehler durchlaufen; baue testweise ohne `--noconsole`, um Logs zu sehen.
* **Icon wird nicht angezeigt**: Stelle sicher, dass `icon.ico` wirklich 256×256 enthält und du **neu baust** (`dist/` vorher löschen).

---

Wenn du willst, passe ich dir das Skript noch an:

* mit **eigenem User-Agent**,
* **Fenster-Icon** im Titel,
* **Splash-Screen** vor dem Laden,
* oder einem **Offline-Hinweis**.
  Sag mir einfach, was du gern hättest – ich schreibe es dir direkt rein.
