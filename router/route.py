# route.py
from http.server import BaseHTTPRequestHandler
import json


class Route:
    @staticmethod
    def GET(route, status_code, header, response):
        return lambda *args, **kwargs: BaseHTTPRequestHandler(
            route, status_code, header, response, *args, **kwargs
        )

    @staticmethod
    def POST(route, status_code, header, response, controller):
        return lambda *args, **kwargs: controller(
            route, status_code, header, response, *args, **kwargs
        )


# this is router
def router():
    return {
        '/': {
            'status_code': 200,
            'header': {'Custom-Header': 'Value'},
            'response': {'status': 'oke'},
        },
        '/hello': {
            'status_code': 200,
            'header': {'Custom-Header': 'Value'},
            'response': {'message': 'Hello, World!'},
        },
    }
