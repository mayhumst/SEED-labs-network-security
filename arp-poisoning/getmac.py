#!/usr/bin/envpython3 
from scapy.all import * 


def get_mac(ip):
    # Create arp packet object. pdst - destination host ip address
    arp_request = ARP(pdst=ip)
    # Create ether packet object. dst - broadcast mac address. 
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine two packets in two one
    arp_request_broadcast = broadcast/arp_request
    # Get list with answered hosts
    answered_list = srp(arp_request_broadcast, timeout=1,
                              verbose=False)[0]
    # Return host mac address
    ans = answered_list[0][1].hwsrc
    print(ans)
    return ans
    
get_mac("10.9.0.5")
