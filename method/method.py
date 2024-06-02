from http.server import BaseHTTPRequestHandler
import json


class GET(BaseHTTPRequestHandler):
    def __init__(self, route, status_code, header, response, *args, **kwargs):
        self.route = route
        self.status_code = status_code
        self.header = header
        self.response = response
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == self.route:
            self.send_response(self.status_code)
            self.send_header('Content-type', 'application/json')
            for key, value in self.header.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(json.dumps(self.response).encode())
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)
