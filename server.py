from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.0.105"
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        # Handling GET request
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))

    def do_POST(self):
        # Handling POST request
        content_length = int(self.headers['Content-Length'])  # Get the length of the incoming data (if any)
        post_data = self.rfile.read(content_length)  # Read the incoming POST data (can be ignored if not needed)
        
        # Sending response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Current timestamp in "YYYY-MM-DD HH:MM:SS" format
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        
        # Sending the JSON response with the timestamp
        response = '{"time": "' + date + '"}'
        self.wfile.write(bytes(response, "utf-8"))

# Create an HTTP server with the specified host and port
server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")

# Start the server
server.serve_forever()

# Close the server (this line won't execute unless the server is stopped manually)
server.server_close()
print("Server stopped")
