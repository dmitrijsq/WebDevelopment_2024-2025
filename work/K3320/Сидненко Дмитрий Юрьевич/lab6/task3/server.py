from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')  # Указываем кодировку
        self.end_headers()

        with open('index.html', 'rb') as file:  # Открываем файл
            self.wfile.write(file.read())


def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print('Сервер запущен на http://localhost:8000')
    httpd.serve_forever()


if __name__ == '__main__':
    run()