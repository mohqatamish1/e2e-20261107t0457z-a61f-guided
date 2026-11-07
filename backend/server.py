import os,json,time
from http.server import BaseHTTPRequestHandler,HTTPServer
import psycopg
if os.getenv('RUNTIME_REQUIRED') != 'ready':
    raise RuntimeError('Missing required runtime variables for backend: RUNTIME_REQUIRED')
for attempt in range(30):
    try:
        with psycopg.connect(os.environ['DATABASE_URL']) as db:
            db.execute('CREATE TABLE IF NOT EXISTS fixture_sentinel (id integer primary key, value text not null)')
            db.execute("INSERT INTO fixture_sentinel VALUES(1,'nas161-preserved') ON CONFLICT(id) DO NOTHING")
        break
    except psycopg.OperationalError:
        if attempt==29:raise
        time.sleep(1)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with psycopg.connect(os.environ['DATABASE_URL']) as db:
            value=db.execute('SELECT value FROM fixture_sentinel WHERE id=1').fetchone()[0]
        self.send_response(200);self.send_header('Access-Control-Allow-Origin','*');self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(json.dumps({'sentinel':value,'runtime':os.environ['RUNTIME_REQUIRED']}).encode())
HTTPServer(('0.0.0.0',8000),Handler).serve_forever()
