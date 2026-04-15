import http.server
import os
import sys

DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
PORT = 8888

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        path = self.path.split("?")[0].split("#")[0]
        full = os.path.join(DIRECTORY, path.lstrip("/"))
        if not os.path.exists(full):
            if os.path.exists(full + ".html"):
                self.path = path + ".html"
            elif os.path.exists(os.path.join(full, "index.html")):
                self.path = path + "/index.html"
            else:
                if os.path.exists(os.path.join(DIRECTORY, "404.html")):
                    self.path = "/404.html"
        super().do_GET()

    def log_message(self, format, *args):
        pass

with http.server.HTTPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
