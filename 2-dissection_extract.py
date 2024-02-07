from scapy.all import *
import os

dns_pkts_analysis = "sample_packets\dns_pkts_analysis.pcap"
packets = rdpcap(dns_pkts_analysis)

# for i, packet in enumerate(packets[:1]):
#     print(f"Packet {i+1}")
#     packet.show()

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
    
for i, packet in enumerate(packets[:15]):
    print(f"Packet {i+1}")
    dissect_packet(packet)