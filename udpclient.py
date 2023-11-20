import socket
import threading
from collections import deque 


received_messages = deque()


def returnReceivedMessages():
    if received_messages:
        msg = received_messages.popleft()
    else:
        msg = ""
    return msg

def receiveMessages():
    
    buffer_size = 1024

    # Create a UDP socket at the client side
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    udp_client_socket.bind(("127.0.0.1", 7500))
    while True:
        try:
            # Receive a message from the server
            msg_from_server, _ = udp_client_socket.recvfrom(buffer_size)
            received_message = msg_from_server.decode('utf-8')
            received_messages.append(received_message)
            
            print("Received message from server:", received_message)

        except socket.error as e:
            print("Error receiving message:", e)


def transmitCode(code):
    # Convert code to string then encode in bytes
    c = str(code)
    bytesToSend = str.encode(c)
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)


UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Main function
serverAddressPort = ("127.0.0.1", 7501)
bufferSize = 1024

receive_thread = threading.Thread(target=receiveMessages, daemon=True)
receive_thread.start()







    


