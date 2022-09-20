# from the socket module import all
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)



server_name = gethostname()
server_IpAddress = gethostbyname(server_name)


# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
server_address = (gethostname(), 10000)

#connects to other student
#server_address = ('Rheeeeeena', 10000)
#server_address = ('DESKTOP-EA5VKRJ', 10000)

# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)

# Connect the socket to the host and port
sock.connect(server_address)

try:

    print(f"Say 'hi' to {server_address[0]}...\nType 'zzz' to end message")
    # Send data
    
    #a flag that checks if the chat is still running
    endMessage = True
    while endMessage:  
        message = input("Me: ")
        # Data is transmitted to the server with sendall()
        # encode() function returns bytes object
        sock.sendall(message.encode())

        # Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(50).decode()
        print(f'{server_address[0]}: {data}')

        #indicator to close the message   
        if data == "zzz" or message == "zzz":
            endMessage = False
            break

    #closing the connection
    if endMessage is False:
        message = 'Connection closing. Bye bye'
        sock.sendall(message.encode())
        print('Connection closing. Bye bye')
        sock.close()

finally:
    sock.close()