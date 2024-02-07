import socket 
from scapy.all import *

# <!-- def process_packet(packet):
#     print(packet.summary())
#     #packet.show()  
#     print() -->

def dissect_packet(packet):
    #print(packet.summary())
    
    # packet.show()
    if Ether in packet:
        print("Source MAC:", packet[Ether].src)
        print("Destination MAC:", packet[Ether].dst)
        
    if IP in packet:
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst) 
        print("Protocol:", packet[IP].proto)   
        
    if UDP in packet:
        print("Source Port:", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)
        # print("Window: ", packet[UDP].window)
    
    if DNS in packet:
        print("DNS Query:", packet[DNS].qd.qname)
        print("DNS Response:", packet[DNS].an.rdata)
        
    print()
    
def capture_live_traffic():
    # sniff(prn=process_packet, store=0)
    sniff(filter="tcp and (port 80 or port 443)", prn=dissect_packet, store=0)
    
if __name__ == "__main__":
    capture_live_traffic()

