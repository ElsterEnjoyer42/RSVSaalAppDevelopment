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
    # Startet das native WebView
    webview.start()

if __name__ == "__main__":
    main()
