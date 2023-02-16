from scapy.layers.dns import DNS
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP
from .models import Packet


def create_packet(packet):
    try:
        ip = packet[IP]
        src_ip = ip.src
        dst_ip = ip.dst
        pkt = Packet(
            src_ip=src_ip,
            dst_ip=dst_ip,
            payload=str(packet)
        )
        pkt.save()
    except Exception as e:
        print(f"Error creating packet: {e}")


def return_url(pkt):
    if pkt.haslayer(HTTPRequest):
        url = pkt[HTTPRequest].Host.decode() + pkt[HTTPRequest].Path.decode()
        return url


def return_dns(pkt):
    if pkt.haslayer(DNS):
        if pkt[DNS].qr == 0:
            query = pkt[DNS].qd.qname.decode()
            return query
