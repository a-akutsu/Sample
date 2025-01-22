from http.server import HTTPServer, CGIHTTPRequestHandler

# CGI ハンドラの設定
httpd = HTTPServer(("localhost", 8080), CGIHTTPRequestHandler)
httpd.serve_forever()
