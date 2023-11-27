import socket
import random
import time

bufferSize  = 1024
serverAddressPort   = ("127.0.0.1", 7501)
clientAddressPort   = ("127.0.0.1", 7500)


print('this program will generate some test traffic for 2 players on the red ')
print('team as well as 2 players on the green team')
print('')

red1 = '89'
red2 = '21'
green1 = '3'
green2 = '5'
greenBase = '43'
redBase = '53'

# Create datagram sockets
UDPServerSocketReceive = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# bind server socket
UDPServerSocketReceive.bind(serverAddressPort)

# wait for start from game software
print ('')
print ('waiting for start from game_software')

received_data = ' '
while received_data != '202':
	received_data, address = UDPServerSocketReceive.recvfrom(bufferSize)
	received_data = received_data.decode('utf-8')
		
	print ('Received from game software: ', received_data)
print ('')

# create events, random player and order

while True:
    
	opposite_team_player_red = None
	opposite_team_player_green = None
 
	if random.randint(1,2) == 1:
		redplayer = red1
		opposite_team_player_red = red1
	else:
		redplayer = red2
		opposite_team_player_red = red2	
	if random.randint(1,2) == 1:
		greenplayer = green1
		opposite_team_player_green = green1
	else: 
		greenplayer = green2
		opposite_team_player_green = green2	
  
	randomInt = random.randint(1, 20)
 
	if randomInt in [1, 5, 9, 15]: 
		message = str(redplayer) + ":" + str(greenplayer)
	elif randomInt in [2, ]:
		message = str(opposite_team_player_green) + ":" + str(greenBase)
	elif randomInt in [3, 8, 11, 17]:  
		message = str(greenplayer) + ":" + str(redplayer)
	elif randomInt in [4, 14]: 
		message = str(opposite_team_player_red) + ":" + str(redBase)
	else:
		continue
    
	UDPClientSocketTransmit.sendto(str.encode(str(message)), clientAddressPort)
	# receive answer from game software
	received_data, address = UDPServerSocketReceive.recvfrom(bufferSize)
	received_data = received_data.decode('utf-8')
	print ('Received from game software: ', received_data)
	print ('')
	if received_data == '221':
		print('Received code: 221')
		print('Received code: 221')
		print('Received code: 221')
		break
	time.sleep(random.randint(1,3))
	
print("program complete")
    
    