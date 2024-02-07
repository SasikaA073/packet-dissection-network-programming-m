import socket
port = 73
address = "127.0.0.1"
BUF_SIZE = 1024


print("---------------------------CLIENT 2 --------------")

# create a socket object name 'con'
con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# establish the connection
con.connect((
    address,port)) # gets a tuple as the argument

data = con.recv(BUF_SIZE)
print(data.decode('utf-8'))

print("Enter the message you want to send to client 1")
messageClient2 = input()
con.send(bytes(messageClient2,'utf-8'))