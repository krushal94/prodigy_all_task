pip install scapy
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Function to analyze each packet
def analyze_packet(packet):
    # Check if it's an IP packet
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # TCP packets
        if TCP in packet:
            print(f"TCP Packet: {ip_src} -> {ip_dst}, Src Port: {packet[TCP].sport}, Dst Port: {packet[TCP].dport}")
        
        # UDP packets
        elif UDP in packet:
            print(f"UDP Packet: {ip_src} -> {ip_dst}, Src Port: {packet[UDP].sport}, Dst Port: {packet[UDP].dport}")
        
        # Other IP packets (ICMP, etc.)
        else:
            print(f"IP Packet: {ip_src} -> {ip_dst}, Protocol: {protocol}")

# Capture packets with sniff (You can change the interface and count)
print("Starting packet capture... Press Ctrl+C to stop.")
sniff(filter="ip", prn=analyze_packet, count=10)  # Captures 10 packets
