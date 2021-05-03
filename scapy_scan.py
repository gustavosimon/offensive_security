#!/usr/bin/python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys
from scapy.all import *

# Checks if received all the necessary parameters
# Usage example: python scapy_scan.py [IP] [INITIAL_PORT] [FINAL_PORT]
if len(sys.argv) != 4:
    print("Correct usage of scapy_scan: python scapy_scan.py [IP] [INITIAL_PORT] [FINAL_PORT]")
    sys.exit(0)

# Get the IP
target_ip = str(sys.argv[1])
# Get the initial port
initial_port = int(sys.argv[2])
# Get the final port
final_port = int(sys.argv[3])

print("Scanning " + target_ip + " looking for TCP open ports\n") 

# If the initial port is equal to the final port increments the final port
if initial_port == final_port:
    final_port += 1 

for i in range(initial_port, final_port):
    packet = IP(dst=target_ip)/TCP(dport=i,flags='S')
# Send the packet and get the first response
# Send a SYN and wait for a SYN-ACK
    response = sr1(packet, timeout=0.5, verbose=0)
# If the response has the TCP layer, and the TCP layer represent a SYN-ACK
    if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        print("Port: " + str(i) + " is open\n")
# Send a packet with the RST
    sr(IP(dst=target_ip)/TCP(dport=response.sport, flags='R'), timeout=0.5, verbose=0)

print("Scan is complete")