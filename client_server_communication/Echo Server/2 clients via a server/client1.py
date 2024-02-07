import socket,time
port = 73
address = "127.0.0.1"
BUF_SIZE = 1024

# create a socket object name 'con'
con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# establish the connection
con.connect((address,port)) # gets a tuple as the argument

message = input("Enter the message that you want to send to client 2 >>>")
con.send(bytes(message,"utf-8")) # send the message using the 'utf-8' encoding method
time.sleep(10)
# This time client1 does not get any response, the response should be directed to client 2
data = con.recv(BUF_SIZE)
print(data.decode('utf-8')) # idk what this means
##    # gets the data maximum he
##    decodedData = data.decode('utf-8')
##    # con.close() # terminates the connectiolhn



