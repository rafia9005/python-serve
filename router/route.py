from http.server import BaseHTTPRequestHandler
import json


class Route:
    @staticmethod
    def GET(route, status_code, header, response):
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == route:
                    self.send_response(status_code)
                    self.send_header('Content-type', 'application/json')
                    for key, value in header.items():
                        self.send_header(key, value)
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self.send_error(404, 'File Not Found: %s' % self.path)

        return Handler
