import sipfullproxy
import socketserver
import socket
import logging

import re

if __name__ == "__main__":

    logging.basicConfig(level=logging.WARNING, filename="zaznam-hovorov.log")

    HOST, PORT = '0.0.0.0', 5060
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print(f"SIP PROXY server {hostname} is running on {ipaddress}" )
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

