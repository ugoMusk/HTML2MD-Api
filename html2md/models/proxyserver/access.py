#!/usr/bin/env python3
""" create a logedout user experience """

import socket

def getUserIp():
    """ get and return user ip address """
    # Creating a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connecting to a remote server; this will obtain the local IP address
        sock.connect(("8.8.8.8", 80))
        # Getting the local IP address and hostname
        ip_address = sock.getsockname()[0]
        hostname = socket.gethostname()
    finally:
        # Closing the socket connection
        sock.close()
        # Return the IP address as a tuple
        return ip_address

if __name__ == "__main__":
    print("imported")
