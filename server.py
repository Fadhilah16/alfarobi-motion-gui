import http.server
import socketserver

PORT = 8000
IP = '127.0.0.1'
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((IP, PORT), handler) as httpd:
    print("Server started at "+IP+":" + str(PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        # Clean-up server (close socket, etc.)
        httpd.server_close()