from http.server import BaseHTTPRequestHandler
from router.route import Route


class CustomHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.routes = server.routes
        super().__init__(request, client_address, server)

    def do_GET(self):
        handler = self.routes.get(self.path)
        if handler:
            handler_instance = handler(
                self.request, self.client_address, self.server
            )
            handler_instance.handle_one_request()
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


def run(server_class=CustomHandler, routes=None, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, routes)

    print(f'Server started on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    routes = {
        '/': Route.GET(
            '/', 200, {'Custom-Header': 'Value'}, {'status': 'oke'}
        ),
        '/hello': Route.GET(
            '/hello',
            200,
            {'Custom-Header': 'Value'},
            {'message': 'Hello, World!'},
        ),
    }
    run(routes=routes)
