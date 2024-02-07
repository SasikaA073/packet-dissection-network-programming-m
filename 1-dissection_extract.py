from scapy.all import *
import os

dns_pkts_analysis = "sample_packets\dns_pkts_analysis.pcap"
packets = rdpcap(dns_pkts_analysis)

for i, packet in enumerate(packets[:1]):
    print(f"Packet {i+1}")
    packet.show()