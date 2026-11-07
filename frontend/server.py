from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import os, urllib.request, json
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/private':
            try:
                body=urllib.request.urlopen(os.environ['INTERNAL_API_URL']+'/sentinel',timeout=10).read()
                self.send_response(200);self.end_headers();self.wfile.write(body)
            except Exception:
                self.send_response(503);self.end_headers();self.wfile.write(b'private dependency unavailable')
            return
        api=Path('api-url').read_text();label=Path('label').read_text()
        body=('<!doctype html><html lang="en"><meta name="viewport" content="width=device-width"><title>NAS-161 fixture</title><body><h1>NAS-161 fixture</h1><p id="label">'+label+'</p><button id="read">Read database sentinel</button><pre id="result"></pre><script>const api='+json.dumps(api)+';document.getElementById("read").onclick=async()=>{document.getElementById("result").textContent=await(await fetch(api+"/sentinel")).text()};</script></body></html>').encode()
        self.send_response(200);self.send_header('Content-Type','text/html');self.end_headers();self.wfile.write(body)
HTTPServer(('0.0.0.0',3000),Handler).serve_forever()
