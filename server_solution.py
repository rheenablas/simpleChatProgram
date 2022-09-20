# from the socket module import all
from socket import *
import datetime

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
server_address = (gethostname(), 10000)
# output to terminal some info on the address details
server_name = gethostname()
server_IpAddress = gethostbyname(server_name)

print(f"Host name:{server_name}\tIp address:{server_IpAddress}")


print(f'*** Server is starting up on {server_name} port {server_address[1]} ***')

# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    

    print('connection from', client_address)
    print("Type 'zzz' to end message")
    try:
        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(50).decode()
            #if data:   

            #get the time stamp using datetime
            timeReceived = str(datetime.datetime.now())   
            #writes the data received from client to a text file called logfile         
            file = open("logfile.txt", 'a')
            file.write(f"{data}\t{timeReceived}\n")
            file.close()

            #prints what the client has said
            print(f'{client_address[0]}: {data}') #on {timeReceived}
            #print('sending data back to the client')
            
            #server sending message
            msg = input("Me: ")
            connection.sendall(msg.encode())

            if data == "zzz" or msg == "zzz": 
                #connection.close()
                sock.close()
                print("Connection closing. Bye bye")
                break
        break

    finally:
        # Clean up the connection
        connection.close()
            

# now close the socket
sock.close()