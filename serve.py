import http.server
import os

DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
PORT = 8888


class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def _resolve_clean_url(self):
        path = self.path.split("?")[0].split("#")[0]
        full = os.path.join(DIRECTORY, path.lstrip("/"))
        if not os.path.exists(full):
            if os.path.exists(full + ".html"):
                self.path = path + ".html"
            elif os.path.exists(os.path.join(full, "index.html")):
                self.path = path + "/index.html"
            elif os.path.exists(os.path.join(DIRECTORY, "404.html")):
                self.path = "/404.html"

    def do_GET(self):
        self._resolve_clean_url()
        super().do_GET()

    def do_HEAD(self):
        self._resolve_clean_url()
        super().do_HEAD()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        pass


with http.server.HTTPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
