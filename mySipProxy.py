import sipfullproxy
import socketserver
import socket
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, filename="dennik-hovorov.log", format='%(asctime)s: %(message)s')

    PORT = 5060
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print(f"SIP PROXY server {hostname} is running on {ipaddress}" )
    sipfullproxy.recordroute = f"Record-Route: <sip:{ipaddress}:{PORT};lr>"
    sipfullproxy.topvia = f"Via: SIP/2.0/UDP {ipaddress}:{PORT}"
    server = socketserver.UDPServer((ipaddress, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

