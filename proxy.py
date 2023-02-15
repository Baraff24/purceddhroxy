from scapy.all import *
from collections import deque

# Define the queue to store the packets
PACKET_QUEUE = deque(maxlen=100)

# Define the filters to check the packets for vulnerabilities
FILTERS = [
    # Detect a potential SQL injection vulnerability in the packet
    lambda packet: "SELECT" in packet[Raw].load.decode("utf-8"),

    # Detect a potential XSS vulnerability in the packet
    lambda packet: "<script>" in packet[Raw].load.decode("utf-8"),

    # Detect a potential vulnerability in the packet User-Agent header
    lambda packet: "Python" in packet[Raw].load.decode("utf-8")

    # Add more filters here
]


# Define the function to filter the packets
def filter_packets(packet):
    # Apply the filters to the packet
    for f in FILTERS:
        if f(packet):
            # If the packet fails any of the filters, print the packet and drop it
            print(packet.show())
            print("Potential attack detected! Packet dropped.")
            return None
    # If the packet passes all the filters, add it to the queue
    PACKET_QUEUE.append(packet)
    return packet


# Define the function to route the packets
def route_packets(packet):
    if packet is not None:
        # Route
        packet_in_queue = PACKET_QUEUE.popleft()
        send(packet_in_queue, verbose=False)


# Start the defense proxy
def start_defense_proxy():
    # Interface of the network card to sniff the packets
    iface = "eth0"
    # Start the sniffing process
    sniff(iface=iface, prn=filter_packets)
    # Start the routing process
    sniff(iface=iface, prn=route_packets)


if __name__ == "__main__":
    start_defense_proxy()
