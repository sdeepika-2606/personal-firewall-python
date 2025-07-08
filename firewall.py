# firewall.py

# firewall.py

from scapy.all import sniff, IP, TCP, UDP, ICMP, conf
import json
from datetime import datetime

# Use pcap to sniff without sudo (on Windows or dev mode)
conf.use_pcap = True

# Load rules from JSON
def load_rules():
    with open("rules.json", "r") as f:
        return json.load(f)

rules = load_rules()

# Log blocked packet
def log_packet(packet, reason):
    with open("firewall_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] Blocked: {packet.summary()} | Reason: {reason}\n")

# Apply firewall rules
def apply_rules(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src

        if src_ip in rules["block_ips"]:
            log_packet(packet, f"Blocked IP {src_ip}")
            return False

        if "ICMP" in rules["block_protocols"] and packet.haslayer(ICMP):
            log_packet(packet, "Blocked ICMP protocol")
            return False

        if packet.haslayer(TCP) or packet.haslayer(UDP):
            port = packet[TCP].dport if packet.haslayer(TCP) else packet[UDP].dport
            if port not in rules["allow_ports"]:
                log_packet(packet, f"Blocked Port {port}")
                return False

    return True

# Callback for sniffed packets
def packet_callback(packet):
    if not apply_rules(packet):
        return
    print(f"[ALLOWED] {packet.summary()}")

print("🔒 Personal Firewall Running (Non-root Mode)...")
sniff(prn=packet_callback, store=0)
