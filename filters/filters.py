from scapy.layers.inet import TCP
from scapy.packet import Raw


# Add your filters here

def filter_sql_injection(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        pkt_str = str(pkt.getlayer(Raw), encoding="utf-8", errors="ignore")
        if "select" in pkt_str or "insert" in pkt_str or "update" in pkt_str or "delete" in pkt_str:
            return True
        else:
            return False


def filter_xss(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        pkt_str = str(pkt.getlayer(Raw), encoding="utf-8", errors="ignore")
        if "<script>" in pkt_str or "</script>" in pkt_str:
            return True
        else:
            return False


def filter_user_agent(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        pkt_str = str(pkt.getlayer(Raw), encoding="utf-8", errors="ignore")
        if "Python" in pkt_str:
            return True
        else:
            return False
