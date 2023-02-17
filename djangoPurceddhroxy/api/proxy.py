from scapy.all import *
from collections import deque

from scapy.layers.inet import IP

from .functions import return_url, return_dns
from .models import Filter

# Define the queue to store the packets
PACKET_QUEUE = deque(maxlen=100)


# Define the function to filter the packets
def filter_packets(pkt):
    # Apply the filters to the packet
    # Apply filters to packet
    filters = Filter.objects.filter(is_active=True)
    for fil in filters:
        function = fil.function
        if function:
            func = eval(function)
            func(pkt)
            if func(pkt):
                # If the packet fails any of the filters, print the packet and drop it
                print(f"Potential attack detected! Packet from {pkt[IP].src} to {pkt[IP].dst}. "
                      f"HTTP request: {return_url(pkt)}."
                      f"DNS request: {return_dns(pkt)}")
                with open("alerts.log", "a") as k:
                    k.write(f"{time.time()}: {pkt.summary()}\n")
                pkt.drop()
                return None
    if pkt is not None:
        # If the packet passes all the filters, add it to the queue
        return pkt


# Define the function to route the packets
def route_packets(pkt):
    if pkt is not None:
        # Route
        packet_in_queue = PACKET_QUEUE.popleft()
        send(packet_in_queue, verbose=False)
        pkt_model = Packet(src_ip=pkt[IP].src, dst_ip=pkt[IP].dst, payload=str(pkt), dangerous=False)
        pkt_model.save()


# Start the proxy
def start_proxy():
    # Interface of the network card to sniff the packets
    iface = "eth0"

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
        # Start the routing process
        sniff(iface=iface, prn=route_packets)
    except Exception as e:
        logging.error('An error occurred: %s', str(e))


if __name__ == "__main__":
    start_proxy()
