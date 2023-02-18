from scapy.layers.dns import DNS
from scapy.layers.http import HTTPRequest


def return_url(pkt):
    if pkt.haslayer(HTTPRequest):
        url = pkt[HTTPRequest].Host.decode() + pkt[HTTPRequest].Path.decode()
        return url


def return_dns(pkt):
    if pkt.haslayer(DNS):
        if pkt[DNS].qr == 0:
            query = pkt[DNS].qd.qname.decode()
            return query
