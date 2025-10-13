Klar 👌 — hier ist eine komplette, moderne **README.md** für dein Projekt
🖥️ **RSV Saal Desktop App** (die Python-basierte Version mit digital signierten Builds via Cosign).

Ich hab sie so aufgebaut, dass sie

* **für GitHub passt**,
* den **technischen Ablauf klar erklärt**,
* **Windows / macOS** beschreibt
* und optional deine künftige Signatur-Automatisierung berücksichtigt.

---

````markdown
# 🖥️ RSV Saal Desktop App

Dies ist die offizielle Desktop-Anwendung des RSV Saal e.V.  
Sie öffnet die Vereins-Website [https://rsv-saal.de](https://rsv-saal.de) in einem eigenen Fenster –  
leicht, schnell und ohne Browser.

---

## 🚀 Features
- Lädt automatisch **https://rsv-saal.de**
- Keine Installation nötig (portable `.exe` / `.app`)
- Minimaler Ressourcenverbrauch dank **PyWebView**
- Optional signierte Builds mit **Sigstore Cosign**

---

## 📦 Installation / Setup

### Voraussetzungen
- **Python 3.9 oder neuer**
- `pip` (Python Package Installer)

### Abhängigkeiten installieren
```bash
pip install pywebview pyinstaller
````

---

## ▶️ Anwendung starten (Development)

```bash
python app.py
```

Die Anwendung öffnet ein Fenster mit der RSV-Saal-Website.

---

## 🧱 Portable Builds

### 🪟 Windows (.exe)

```bash
pyinstaller --onefile --noconsole --name "RSV Saal" --icon=icon.ico app.py
```

→ Ergebnis: `dist/RSV Saal.exe`

### 🍎 macOS (.app / .dmg)

```bash
pyinstaller --onefile --windowed --name "RSV Saal" --icon=icon.icns app.py
hdiutil create -volname "RSV Saal" -srcfolder "dist/RSV Saal.app" -ov -format UDZO "RSV Saal.dmg"
```

---

## 🔐 Optionale Signierung (Integrität / Open-Source-Proof)

Zur Sicherstellung der Integrität kann die `.exe` mit **[Sigstore Cosign](https://docs.sigstore.dev)** signiert werden.

### Installation von Cosign (Windows)

```powershell
winget install sigstore.cosign
```

oder manuell von
👉 [https://github.com/sigstore/cosign/releases/latest](https://github.com/sigstore/cosign/releases/latest)
nach `C:\Program Files\Cosign\cosign.exe` legen und `PATH` ergänzen.

### Datei signieren

```powershell
cosign sign-blob --yes RSV-Saal.exe > RSV-Saal.exe.sig
```

### Signatur prüfen

```powershell
cosign verify-blob --signature RSV-Saal.exe.sig RSV-Saal.exe
```

Ausgabe bei Erfolg:

```
Verified OK
Cert subject: https://github.com/<deinGitHubAccount>
```

*(Hinweis: Der manuelle GitHub-Login-Flow von Sigstore kann je nach Version variieren; siehe [docs.sigstore.dev](https://docs.sigstore.dev/cosign/signing/overview/).)*

---

## 🧩 Projektstruktur

```
rsv-desktop/
│
├─ app.py              # Hauptdatei (PyWebView)
├─ icon.ico            # App-Icon (Windows)
├─ icon.icns           # App-Icon (macOS)
├─ README.md
└─ dist/               # Build-Ausgabe
```

---

## ⚙️ Bekannte Hinweise

| Problem                                 | Lösung                                                                                                           |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Windows blockiert `.exe`                | Rechtsklick → Eigenschaften → „Zulassen“                                                                         |
| SmartScreen-Warnung                     | Normal bei unsignierten Dateien                                                                                  |
| macOS: „nicht verifizierter Entwickler“ | Rechtsklick → Öffnen → Trotzdem öffnen                                                                           |
| „No WebView2 runtime found“             | [WebView2 Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-section) installieren |

---

## 📂 Downloads

| Plattform  | Datei                                           | Beschreibung                       |
| ---------- | ----------------------------------------------- | ---------------------------------- |
| 🪟 Windows | [RSV Saal.exe](./public/downloads/RSV-Saal.exe) | Portable Version ohne Installation |
| 🍎 macOS   | [RSV Saal.dmg](./public/downloads/RSV-Saal.dmg) | Drag-and-Drop-Installation         |
| 📱 Android | [RSV Saal.apk](./public/downloads/RSV-Saal.apk) | Beta-App mit WebView               |

---

## 🧑‍💻 Autor

**Julian Bujara**
Projekt RSV Saal e.V.
[https://rsv-saal.de](https://rsv-saal.de)

---

## 📝 Lizenz

MIT License – frei zur Nutzung und Anpassung.

```

---

Willst du, dass ich noch **eine erweiterte GitHub-README-Version** mit:
- Badges (Build Status, Download-Zähler),
- Screenshots deiner App,
- automatischer Release-Signierung per GitHub Actions  
erstelle?
```
