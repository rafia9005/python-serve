from http.server import BaseHTTPRequestHandler
from handler.TestController import GET as TestGet  # Perbaikan sintaks import


class Route:
    @staticmethod
    def GET(route, status_code, header, response):
        return lambda *args, **kwargs: TestGet(
            route, status_code, header, response, *args, **kwargs
        )

    @staticmethod
    def POST(route, status_code, header, response, controller):
        return lambda *args, **kwargs: controller(
            route, status_code, header, response, *args, **kwargs
        )


def router():
    return {
        '/': {
            'status_code': 200,
            'header': {'Custom-Header': 'Value'},
            'response': TestGet(),  # Menggunakan handler TestController
        },
        '/hello': {
            'status_code': 200,
            'header': {'Custom-Header': 'Value'},
            'response': {'message': 'Hello, World!'},
        },
    }
