from scapy.layers.inet import TCP
from scapy.packet import Raw


# Add your filters here

def sql_injection(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        load = pkt.getlayer(Raw).load
        if "select" in load or "insert" in load or "update" in load or "delete" in load:
            return True
        else:
            return False


def xss(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        load = pkt.getlayer(Raw).load
        if "<script>" in load:
            return True
        else:
            return False


def user_agent(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        load = pkt.getlayer(Raw).load
        if "Python" in load:
            return True
        else:
            return False
