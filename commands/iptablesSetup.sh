#!/usr/bin/env bash

# This script is used to set up iptables and start the proxy
echo -e "\e[34m >>> Setting up the iptables for the proxy... \e[97m"
iptables -I INPUT -j NFQUEUE --queue-num 1
iptables -I OUTPUT -j NFQUEUE --queue-num 1
iptables -I FORWARD -j NFQUEUE --queue-num 1
echo -e "\e[32m >>> iptables setup completed \e[97m"
echo -e "\e[34m >>> Starting the proxy... \e[97m"
exec python proxy/proxy.py