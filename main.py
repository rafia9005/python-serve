from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class CustomHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, routes=None, **kwargs):
        self.routes = routes if routes is not None else {}
        super().__init__(*args, **kwargs)

    def do_GET(self):
        route = self.routes.get(self.path)
        if route:
            self.send_response(route['status_code'])
            self.send_header('Content-type', 'application/json')
            for key, value in route['header'].items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(json.dumps(route['response']).encode())
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


def run(server_class=HTTPServer, handler_class=CustomHandler, routes=None, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, lambda *args, **kwargs: handler_class(*args, routes=routes, **kwargs))

    print(f'Server started on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    routes = {
        '/': {
            'status_code': 200,
            'header': {'Custom-Header': 'Value'},
            'response': {'status': 'oke'}
        },
        '/hello': {
            'status_code': 200,
            'header': {'Custom-Header': 'Value'},
            'response': {'message': 'Hello, World!'}
        },
    }
    run(routes=routes)

