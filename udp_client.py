# UDP Client Example

import socket

target_host = "127.0.0.1"
target_port = 80

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto("AAABBBCCC",(target_host, target_port))

# Receive data
data, addr = client.recvfrom(4096)

print data