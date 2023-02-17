from scapy.layers.inet import TCP
from scapy.packet import Raw


# Add your filters here

def filter_sql_injection(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        pkt_str = pkt.getlayer(Raw).load.decode('ISO-8859-1')
        if "select" in pkt_str or "insert" in pkt_str or "update" in pkt_str or "delete" in pkt_str:
            return True
        else:
            return False


def filter_xss(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        pkt_str = pkt.getlayer(Raw).load.decode('ISO-8859-1')
        if "<script>" in pkt_str or "</script>" in pkt_str:
            return True
        else:
            return False


def filter_user_agent(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        pkt_str = pkt.getlayer(Raw).load.decode('ISO-8859-1')
        if "Python" in pkt_str:
            return True
        else:
            return False
