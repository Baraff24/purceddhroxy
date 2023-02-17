from scapy.all import *
from collections import deque

from scapy.layers.dns import DNS
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP

import filters.filters


def return_url(pkt):
    if pkt.haslayer(HTTPRequest):
        url = pkt[HTTPRequest].Host.decode() + pkt[HTTPRequest].Path.decode()
        return url


def return_dns(pkt):
    if pkt.haslayer(DNS):
        if pkt[DNS].qr == 0:
            query = pkt[DNS].qd.qname.decode()
            return query


# Define the function to filter the packets
def filter_packets(pkt):

    # Apply the filters to the packet
    # Apply filters to packet
    for i in dir(filters.filters):
        fil = getattr(filters.filters, i)
        if callable(fil) and i.startswith("filter"):
            fil(pkt)
            if fil(pkt):
                # If the packet fails any of the filters, print the packet and drop it
                print(
                    f"Potential attack detected! Packet from {pkt[IP].src} to {pkt[IP].dst}. HTTP request: {return_url(pkt)}. DNS request: {return_dns(pkt)}")
                with open("alerts.log", "a") as k:
                    k.write(f"{time.time()}: {pkt.summary()}\n")
                pkt.drop()
                return None
    if pkt is not None:
        # If the packet passes all the filters, add it to the queue
        return pkt


# Start the proxy
def start_proxy():
    # Interface of the network card to sniff the packets

    # wireless interface for mac
    iface = "en0"
    # interface for linux
    # iface = "eth0"

    # Check if the interface exists
    try:
        get_if_hwaddr(iface)
    except OSError:
        logging.error(f"Interface {iface} does not exist")
        exit(1)

    # Check if the interface is up
    try:
        get_if_addr(iface)
    except OSError:
        logging.error(f"Interface {iface} is down")
        exit(1)

    try:
        # Start the sniffing process
        sniff(iface=iface, prn=filter_packets)
    except Exception as e:
        logging.error('An error occurred: %s', str(e))


if __name__ == "__main__":
    start_proxy()
