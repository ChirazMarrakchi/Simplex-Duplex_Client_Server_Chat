from socket import *
import sys
import threading
flag = False
# function for receiving message from client
def recv_from_client(conn):
	
	try:
		# Receives the request message from the client
		message = conn.recv(1024).decode()
		# if 'q' is received from the client the server quits
		if message == 'q':
			conn.send('q'.encode())
			print('Closing connection')
			conn.close()
			flag = True
		print('Message Received: ' + message)
	except:
		conn.close()


# function for receiving message from client
def send_to_client(conn):
	
	try:
		send_msg = input('Type Message: ')
		# the server can provide 'q' as an input if it wish to quit
		if send_msg == 'q':
			conn.send('q'.encode())
			print('Closing connection')
			conn.close()
			flag = True
		conn.send(send_msg.encode())
	except:
		conn.close()


# this is main function
"""
the main function creates a socket for a duplex connection
threads 1 , threads 2 are lists that appends new tasks in every step :) 
using ta.start() wa.start ()[threads] we can run the two functionalities parralelly 
these functions are run parallely in a loop that breaks if a flag is true 
(i.e the client / server message is  equal to q)
similarly in chatClientDuplex.py code

"""
def main():
    
    HOST = "localhost"
    
    serverPort1 = 13011
    serverSocket1 = socket(AF_INET,SOCK_STREAM)
    
    serverSocket1.bind(('',serverPort1))
    serverSocket1.listen(1)
    
    print('The chat server is ready to connect to a chat client')
    
    connectionSocket1, addr = serverSocket1.accept()
    
    print('Server is connected with a chat client\n')

    threads1 =[]
    threads2 = []


    while True : 
        ta = threading.Thread(target = recv_from_client, args = (connectionSocket1,))
        wa = threading.Thread(target = send_to_client, args =(connectionSocket1,))
        threads1.append(ta)
        ta.start()
        if flag == True :
            break
        threads2.append(wa)
        wa.start()
        if flag == True :
            break
    

    

    
        
    
    serverSocket1.close()
    sys.exit()
    
    


# This is where the program starts
if __name__ == '__main__':
	main()
