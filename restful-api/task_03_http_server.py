#!/usr/bin/python3
"""Module that implements a simple HTTP API server."""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle HTTP GET requests for a simple API."""

    def do_GET(self):
        """Handle GET requests depending on the requested endpoint."""

        # Root endpoint: returns a simple text message.
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Data endpoint: returns a JSON object.
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # Status endpoint: returns a simple OK message.
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Info endpoint: returns basic API information.
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Unknown endpoint: returns a 404 error.
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    # Server configuration: listen on port 8000.
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)

    # Start the server and keep it running.
    print("Server running on port 8000...")
    httpd.serve_forever()
