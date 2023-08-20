import subprocess
import json
import time
import socket

host = '192.168.1.73'
port = 1234
running = True

while running:
    cmd = subprocess.check_output("termux-location")
    js = json.loads(cmd)
    lat = js["latitude"]
    long = js["longitude"]


    location_data = {"latitude": lat, "longitude": long}
    location_json = json.dumps(location_data)
    location_bytes = location_json.encode('utf-8')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(location_bytes)
    s.close()

