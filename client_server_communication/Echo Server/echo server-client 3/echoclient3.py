import socket
port = 1234
address = "127.0.0.1"
BUF_SIZE = 1024

status = True
while True:
# create a socket object name 'con'
    con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # establish the connection
    con.connect((address,port)) # gets a tuple as the argument

    message = input("Enter the message that you want to bounce back >>>")
    con.send(bytes(message,"utf-8")) # send the message using the 'utf-8' encoding method


    data = con.recv(BUF_SIZE) # idk what this means
    # gets the data maximum he
    decodedData = data.decode('utf-8')
    # con.close() # terminates the connectiolhn
    

    print(decodedData) 
    if decodedData.lower() == 'exit':
        # status = False
        # con.close()
        break