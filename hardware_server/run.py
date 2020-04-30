#!/usr/bin/python3
import sys
import os.path
import http.server
from http.server import BaseHTTPRequestHandler
import socketserver
import argparse
import threading

from arduino_connection import ArduinoConnection, ArduinoConnectionError
from listen_serial import listen_serial


parser = argparse.ArgumentParser(description='arduino microclimate server')
parser.add_argument('port', type=int, help='port to connections')                   

args = parser.parse_args()

PORT = args.port
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        request_path = os.path.join(BASE_DIR, self.path[1:])
        print(request_path, self.path, BASE_DIR)
        if os.path.isfile(request_path):
            self.send_response(200, 'ok')
            self.end_headers()
            with open(request_path, 'rb') as file:
                content = file.read()
                self.wfile.write(content)
        else:
            self.send_response(400)
            self.end_headers()
        
    def do_OPTIONS(self):
        self.send_header('Allow', 'GET')
        self.end_headers()
        self.send_response(200, 'ok')


class Server():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5

        self.listen_serial_thread = threading.Thread(target=listen_serial, daemon=True)

    def run(self):
        try:
            with socketserver.TCPServer(('', PORT), Handler) as httpd:
                self.listen_serial_thread.start()
                print("Serving at port", PORT)
                httpd.serve_forever()
        except (KeyboardInterrupt, SystemExit):
            httpd.shutdown()
            print('\nServer shutted down')
            sys.exit()


if __name__ == "__main__":
    connection = ArduinoConnection()

    try:
        connection.connect()
    except ArduinoConnectionError:
        # The last attempt to reconnect. There are sometimes issues
        # with connection from the first time
        connection.connect()

    Server().run()
