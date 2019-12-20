#
# RudePortScanner
#
# Autor: Tiago Almeida (tiagovdaa@gmail.com)
# https://github.com/tiagovdaa/rudeportscanner.git
#

import socket
import sys


def connect_to_ip(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        return sock

    except Exception:
        return None


def scan_port(ip, port, timeout):
    socket.setdefaulttimeout(timeout)
    sock = connect_to_ip(ip, port)

    if sock:
        print('Successfull connect to ' + str(ip) +' on port: '+ str(port))
        sock.close()
    else:
        print('Unable to connect to ' + str(ip) +' on port: '+ str(port))


# Get the IP / domain from the user
ip_domain = input("Enter the ip or domain: ")
if ip_domain == '':
    print('You must specify a host!')
    sys.exit(0)

# Get the port range from the user
port = input("Enter the port range (Ex 20-80): ")
if port == '':
    print('You must specify a port range!')
    sys.exit(0)

# Optional: Get the timeout from the user
timeout = input("Timeout (Default=5): ")
if not timeout:
    timeout = 5

port_range = port.split("-")

# Get the IP address if the host name is a domain
try:
    ip = socket.gethostbyname(ip_domain)
except Exception:
    print('There was an error resolving the domain')
    sys.exit(1)

# If the user only entered one port we will only scan the one port
# otherwise scan the range
if len(port_range) < 2:
    scan_port(ip, int(port), int(timeout))
else:
    for port in range(int(port_range[0]), int(port_range[1])+1):
        scan_port(ip, int(port), int(timeout))
