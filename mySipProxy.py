

import socketserver
import socket
import sys
import time
import logging
from sipfullproxy import UDPHandler

HOST, PORT = '0.0.0.0', 5060

if __name__ == "__main__":

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
    server.serve_forever()
