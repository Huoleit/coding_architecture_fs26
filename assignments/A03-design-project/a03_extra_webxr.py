import http.server
import socket
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to actually connect
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    local_ip = get_local_ip()
    print(f"INFO:     Started server process")
    print(f"INFO:     Serving HTTP on 0.0.0.0 port {PORT}")
    print(f"INFO:     Local:   http://localhost:{PORT}/")
    print(f"INFO:     Network: http://{local_ip}:{PORT}/")
    print(f"INFO:     Waiting for connections...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nINFO:     Shutting down gracefully...")
