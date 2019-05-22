# By: Olivia Zurek, ocz2, section 001 
# UDP Client

import sys
from socket import *

# Counter to count timeout messages
count = 0

# Get the server IP address, port, and length as command line arguments
argv = sys.argv
ip = argv[1]
port = argv[2]
length = argv[3]

# Command line argument is a string, change the port and length into integer
port = int(port)
length = int(length)
data = 'X' * length # Initialize data to be sent

# Create UDP client socket for server.
clientsocket = socket(AF_INET, SOCK_DGRAM)

while count < 3:
    try:
        # Try to connect and catch timeout error
        clientsocket.settimeout(1)
        clientsocket.connect((ip, port))

        # Sending data to server
        print("Sending data to " + ip + ", " + str(port) + ": " + data)
        clientsocket.sendto(data.encode(),(ip, port))
                    
        # Receive the server response
        dataEcho , address = clientsocket.recvfrom(length)

        # Display the server response as an output
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        break
    
    except timeout:
        count += 1
        print("Message timed out")
#Close the client socket
clientsocket.close() 
