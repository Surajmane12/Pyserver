from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.0.105"
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
     
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))

    def do_POST(self):
      
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        
       
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

      
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        
       
        response = '{"time": "' + date + '"}'
        self.wfile.write(bytes(response, "utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")


server.serve_forever()


server.server_close()
print("Server stopped")
