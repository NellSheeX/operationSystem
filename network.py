from scapy.all import *
import time

packed_received = 0
packed_sent = 0

def packed_function(packet):
    global packed_received
    if packet.haslayer(IP):
        packed_received += 1


target_ip = '192.168.1.1'
ping_pkt = IP(dst=target_ip)/ICMP()
send(ping_pkt)


duration = int(11)
start_time = time.time()
while time.time() - start_time < duration:
    sniff(prn=packed_function, timeout=1) 
    packed_sent += 1
    ping_pkt = IP(dst=target_ip)/ICMP()
    send(ping_pkt)


print(f"packed_received : {packed_received} - packed_sent : {packed_sent}")
