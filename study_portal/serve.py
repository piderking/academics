"""
Study Portal Server & Browser Launcher
Serves the Study Portal locally on port 8080 and opens the browser.
"""

import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 8080
DIRECTORY = Path(__file__).resolve().parent


class StudyPortalHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def log_message(self, format, *args):
        # Quiet logger
        pass


def launch():
    os.chdir(DIRECTORY)
    server = HTTPServer(("127.0.0.1", PORT), StudyPortalHandler)
    url = f"http://localhost:{PORT}/index.html"
    print(f"\n=======================================================")
    print(f"  Academic Study Portal is LIVE at: {url}")
    print(f"  Press Ctrl+C to stop the server.")
    print(f"=======================================================\n", flush=True)

    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Study Portal server...")
        server.server_close()


if __name__ == "__main__":
    launch()
