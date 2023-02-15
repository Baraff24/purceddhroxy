from scapy.all import *
from collections import deque

from scapy.layers.dns import DNS
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP, TCP

# Define the queue to store the packets
PACKET_QUEUE = deque(maxlen=100)

# Define the filters to check the packets for vulnerabilities
FILTERS = [
    # Detect a potential SQL injection vulnerability in the packet
    lambda pkt: pkt.haslayer(TCP) and pkt.haslayer(Raw) and "SELECT" in pkt.getlayer(Raw).load,

    # Detect a potential XSS vulnerability in the packet
    lambda pkt: pkt.haslayer(TCP) and pkt.haslayer(Raw) and "<script>" in pkt.getlayer(Raw).load,

    # Detect a potential vulnerability in the packet User-Agent header
    lambda pkt: pkt.haslayer(TCP) and pkt.haslayer(Raw) and "Python" in pkt.getlayer(Raw).load

    # Add more filters here
]


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
    for f in FILTERS:
        if f(pkt):
            # If the packet fails any of the filters, print the packet and drop it
            print(
                f"Potential attack detected! Packet from {pkt[IP].src} to {pkt[IP].dst}. HTTP request: {return_url(pkt)}. DNS request: {return_dns(pkt)}")
            with open("alerts.log", "a") as k:
                k.write(f"{time.time()}: {pkt.summary()}\n")
            return None
    # If the packet passes all the filters, add it to the queue
    PACKET_QUEUE.append(pkt)
    return pkt


# Define the function to route the packets
def route_packets(pkt):
    if pkt is not None:
        # Route
        packet_in_queue = PACKET_QUEUE.popleft()
        send(packet_in_queue, verbose=False)


# Start the proxy
def start_proxy():
    # Interface of the network card to sniff the packets
    iface = "eth0"

    # Start the sniffing process
    sniff(iface=iface, prn=filter_packets)
    # Start the routing process
    sniff(iface=iface, prn=route_packets)


if __name__ == "__main__":
    start_proxy()
