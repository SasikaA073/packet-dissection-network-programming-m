import socket
port = 1234
address = "127.0.0.1"
BUF_SIZE = 3

# create a socket object name 'server'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# creates the server
server.bind((address,port))
server.listen(5) # listens max upto 5 clients at the same time
print("Listening...")

while True:
    con,addr = server.accept() # accept the clients;
    # con is a socket object , addr is a string value : the ip address ig
    print("Connection Address is:",addr)

    data = con.recv(BUF_SIZE) # get the data from the client
    print(data.decode("utf-8")) # decode that data
    decodedData = data.decode('utf-8')
    con.send(data)