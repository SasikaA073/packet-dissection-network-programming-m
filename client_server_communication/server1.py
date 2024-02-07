import socket

from cv2 import add

port = 73
address = "127.0.0.1"

#create a socket object named 'server'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# establish the connection
server.bind((address,port))  # why why?

# listen upto max 5 clients simulatneously, if more than 5 server not working I guess
server.listen(5)
print("Listening...")

while True:
    con,addr = server.accept()
    print("Connection Address is:",addr)
    con.send(bytes("Hello!❤️, Welcome to the server!","utf-8"))
    # BECAUSE OF UTF-8 , we can use emojis in the text I guess(any unicode character)

