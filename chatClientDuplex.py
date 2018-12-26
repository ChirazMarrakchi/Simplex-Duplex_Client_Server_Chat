from socket import *
import sys
import threading


# function for receiving message from client
def send_to_server(clsock):
    send_msg = input('Type Message: ')
    clsock.sendall(send_msg.encode())

# function for receiving message from server
def recv_from_server(clsock):
    data = clsock.recv(1024).decode()
    if data == 'q':
        print('Closing connection')
        sys.exit()
    print('Message Received: ', data)

# this is main function
def main():
    # TODO (1) - define HOST name, this would be an IP address or 'localhost' (1 line)
    HOST = "localhost"
    # TODO (2) - define PORT number (1 line) (Google, what should be a valid port number) 
    PORT1 = 13011
    

    # Create a TCP client socket
	#(AF_INET is used for IPv4 protocols)
	#(SOCK_STREAM is used for TCP)
    # TODO (3) - CREATE a socket for IPv4 TCP connection (1 line)
    clientSocket1 = socket(AF_INET, SOCK_STREAM)
    

    # request to connect sent to server defined by HOST and PORT
    # TODO (4) - request a connection to the server (1 line)
    clientSocket1.connect((HOST,PORT1))
    
    print('Client is connected to a chat server!\n')
    th1 = []
    th2 = []

    while True :
        t1 = threading.Thread(target = send_to_server, args =(clientSocket1,))
        t2 = threading.Thread(target = recv_from_server , args =(clientSocket1,))
        th1.append(t1)
        th2.append(t2)
        t1.start()
        t2.start()

    


    
        
        



# This is where the program starts
if __name__ == '__main__':
    main()
