from scapy.all import *
from scapy.layers.inet import IP

from djangoapp.api.functions import return_url, return_dns
from djangoapp.api.models import Filter
from djangoapp.djangoPurceddhroxy.settings import DJANGO_WS_URL

import websocket
import json


# Define the function to route the packets to the Django server
def send_packet_to_django(pkt):
    # Start the WebSocket connection with the Django server
    ws = websocket.create_connection(DJANGO_WS_URL)

    # Send the packet to the Django server as a JSON object
    ws.send(json.dumps(pkt))

    # Receive the response from the Django server
    result = ws.recv()

    # Close the WebSocket connection with the Django server
    ws.close()

    return result


# Define the function to filter the packets
def filter_packets(pkt):
    # Apply the filters to the packet
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

                # Send the packet to the Django server and transform the packet to a Django model object
                send_packet_to_django(pkt)
                pkt.drop()
                return None
    if pkt is not None:
        # If the packet passes all the filters, add it to the queue
        return pkt


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
        # Start the routing process to the Django server
        sniff(iface=iface, prn=send_packet_to_django)
    except Exception as e:
        logging.error('An error occurred: %s', str(e))


if __name__ == "__main__":
    start_proxy()
