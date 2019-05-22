#By: Olivia Zurek, ocz2, section 001
#UDP Server

import sys
from socket import *

serverIP = '' # use any local ip
serverPort = 12000
dataLen = 100

# Create a UDP socket.
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
print('The server is ready to receive on port: ' + str(serverPort))

while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(dataLen)
    print("Receive data from client " + address[0] + ", " + str(address[1]) + ": " + data.decode())

    # Echo back to client
    print("Sending data to client " + address[0] + ", " + str(address[1]) + ": " + data.decode())
    serverSocket.sendto(data,address) 
