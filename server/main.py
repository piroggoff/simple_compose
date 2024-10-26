import http.server
import socketserver


handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", 1234), handler) as httpd:
    print(f"Quit only with CTRL+C or hanging port will be created\n address {httpd.server_address}")
    httpd.serve_forever()
   