#!/usr/bin/python3

import http.server
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler.

    Inherits from BaseHTTPRequestHandler.
    """

    def do_GET(self):
        """
        Handles GET requests.

        This method checks the path of the request and responds accordingly.
        """

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "This is a simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'404 Not Found')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Runs the HTTP server.

    Args:
        server_class (class): The HTTP server class.
        handler_class (class): The request handler class.
        port (int): The port number to run the server on.

    Returns:
        None
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()

