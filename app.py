
from http.server import BaseHTTPRequestHandler, HTTPServer

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My DevOps Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2ff;
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 8px 25px #00000018;
            max-width: 500px;
            margin: 20px;
        }
        h1 { color: #2563eb; }
        button {
            background: #2563eb;
            color: white;
            padding: 12px 22px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        #message { color: #15803d; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>My DevOps Practice Website</h1>
        <p>My first website running inside a Docker container!</p>
        <button onclick="document.getElementById('message').textContent =
        'Success! Your website is running.'">
            Test Website
        </button>
        <p id="message"></p>
    </div>
</body>
</html>
"""


class WebsiteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404, "Page not found")
            return

        body = HTML.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer(("0.0.0.0", 5000), WebsiteHandler)
print("Website running on port 5000", flush=True)
server.serve_forever()
