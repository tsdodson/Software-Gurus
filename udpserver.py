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
    code = bytesAddressPair[0]
    code = int(code)
    if code == 202:
        print("Game has started:{}".format(code))
    elif code == 221:
        print("Game has ended:{}".format(code))
        print(code)
        print(code)
    else:
        print(code)
    
    