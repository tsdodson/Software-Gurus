import socket

serverAddressPort = ("127.0.0.1", 7500)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def transmitCode(code):

    # Convert code to string then encode in bytes
    c = str(code)
    bytesToSend = str.encode(c)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)


