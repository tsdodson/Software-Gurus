import socket

localIP = "127.0.0.1"
localPort = 7500 #20001 
bufferSize = 1024

# Create a socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming messages
while(True):
    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    equipmentCode = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(equipmentCode)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(equipmentCode)
    print(clientIP)
    