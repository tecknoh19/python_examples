# TCP Server Example

# To test this script, you can connect to it with the putty client for windows.
# With the script running, use putty to connect to 127.0.0.1 port 9999 using a RAW connection
# You can send data from putty by simply typing in the putty window followed by <enter> 

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen(5) # set maximum log of connections to X, in this case, 5

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# Client handling threading
def handle_client(client_socket):
	# Print the data received from the client
	request = client_socket.recv(1024)
	print "[*] Received: %s" % request
	
	# Send a return packet
	client_socket.send("ACK!")
	
	client_socket.close()
	
while True:
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
	
	# Start thread to handle incoming data
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
