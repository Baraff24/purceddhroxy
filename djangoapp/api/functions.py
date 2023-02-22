from scapy.layers.dns import DNS
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP, TCP
from .models import Packet
from .serializers import PacketSerializer


def return_url(pkt):
    if pkt.haslayer(HTTPRequest):
        url = pkt[HTTPRequest].Host.decode() + pkt[HTTPRequest].Path.decode()
        return url


def return_dns(pkt):
    if pkt.haslayer(DNS):
        if pkt[DNS].qr == 0:
            query = pkt[DNS].qd.qname.decode()
            return query


def parse_packet(pkt):
    # Use Scapy to extract relevant data from the packet
    if pkt.haslayer(IP):
        source_address = pkt[IP].src
        destination_address = pkt[IP].dst
        protocol = pkt[IP].proto
        payload = str(pkt[TCP].payload)

    elif pkt.haslayer(DNS):
        source_address = pkt[DNS].an.rdata
        destination_address = pkt[DNS].qd.qname
        protocol = pkt[DNS].qr
        payload = str(pkt[DNS].qd.qname)

    elif pkt.haslayer(HTTPRequest):
        source_address = pkt[HTTPRequest].Host.decode()
        destination_address = pkt[HTTPRequest].Path.decode()
        protocol = pkt[HTTPRequest].Method.decode()
        payload = str(pkt[HTTPRequest].Host.decode())

    else:
        source_address = None
        destination_address = None
        protocol = None
        payload = None

    # Create a Packet object and save it to the database
    pkt_obj = Packet.objects.create(
        src_ip=source_address,
        dst_ip=destination_address,
        type=protocol,
        payload=payload
    )

    # Serialize the DangerousPacket object using Django Serializer
    serializer = PacketSerializer(pkt_obj)
    serialized_packet = serializer.data

    return serialized_packet
