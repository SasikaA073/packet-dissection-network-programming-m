import socket
port = 73
address = "127.0.0.1"
BUF_SIZE = 1024

# create a socket object name 'server'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# creates the server
server.bind((address,port))
server.listen(5) # listens max upto 5 clients at the same time
print("Listening...")

while True:
    print("Connect the first client")
    con1,addr1 = server.accept() # accept the clients;
    # con is a socket object , addr is a string value : the ip address ig
    print("Connection for the client 1 Address is:",addr1)

    data1 = con1.recv(BUF_SIZE) # get the data from the client
     
    decodedData1 = data1.decode('utf-8') # decode that data
##    print(decodedData1)

    print("Connect the second client")
    con2,addr2 = server.accept()
    print("Connection for the client 2 Address is:",addr2)

    con2.send(bytes(decodedData1,'utf-8'))

    # get the data from the client 2
    data2 = con2.recv(BUF_SIZE)
    # decodedData2 = data2.decode("utf-8")
    con1.send(data2)
    
    
