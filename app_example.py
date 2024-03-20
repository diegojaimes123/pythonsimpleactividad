from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hola Mundo</title>
        </head>
        <body>
            <h1>Hi!  ¡Python! solo jajajaj</h1>
        </body>
        </html>
        """

        self.wfile.write(html.encode('utf-8'))

def run_server():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Corriendo en el 3000 :3')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run_server()
