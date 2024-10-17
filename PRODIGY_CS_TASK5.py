pip install scapy

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Function to analyze each packet
from scapy.all import rdpcap

# Read the uploaded PCAP file (change 'yourfile.pcap' to the name of your uploaded file)
packets = rdpcap('/content/ws-4-c2_00001_20230926174511311.pcap')

# Analyze first 10 packets (you can change the range)
for i, packet in enumerate(packets[:10]):
    print(f"Packet {i+1}:")
    packet.show()  # Display detailed info about each packet

tcp_packets = [pkt for pkt in packets if pkt.haslayer('TCP')]
print(f"Total TCP Packets: {len(tcp_packets)}")

ip_src = [pkt['IP'].src for pkt in packets if pkt.haslayer('IP')]
ip_dst = [pkt['IP'].dst for pkt in packets if pkt.haslayer('IP')]
print(f"Source IPs: {set(ip_src)}")
print(f"Destination IPs: {set(ip_dst)}")
