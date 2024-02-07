# 7-client.py
import socket 

server_ip = "212.104.229.115"
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_address = ("127.0.0.1", 12345)
    server_address = (server_ip, 12345)
    
    client_socket.connect(server_address)
    
    with open("to_sent.txt",'rb') as file:
        data = file.read(1000)
        
        while data:
            client_socket.sendall(data)
            data = file.read(1000)
            
    print("File sent successfully")
    client_socket.close()
    
if __name__ == "__main__":
    start_client()