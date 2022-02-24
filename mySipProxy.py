# from MTAA_SIPProxy.sipfullproxy import *
# from sipfullproxy import
import sipfullproxy
import socketserver
import socket



if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 5060
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print(hostname, ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()
