import socket
try:
    import http.server as server
    from http.server import CGIHTTPRequestHandler
except:
    import BaseHTTPServer as server
    from CGIHTTPServer import CGIHTTPRequestHandler

class RequestHandler(CGIHTTPRequestHandler):
    def translate_path(self, path):
        return CGIHTTPRequestHandler.translate_path(self, path)

class NonBlockingServer(server.HTTPServer):
    def __init__(self, *args, **kw):
        server.HTTPServer.__init__(self, *args, **kw)
        self.socket.settimeout(0.032)

    def get_request(self):
        try:
            sock, addr = self.socket.accept()
            sock.settimeout(None)
            return (sock, addr)
        except socket.timeout:
            pass

    def serve_forever(self, *args):
        self.handle_request()

def get_server(port=8000):
    server_address, handler = ('', port), RequestHandler
    return NonBlockingServer(server_address, handler)

