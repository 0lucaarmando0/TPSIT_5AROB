import socket
import threading

server_ip = "192.168.88.106"
server_port = 6000

def client():
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect((server_ip,server_port))

    while True:
        msg = input(">>")
        c.sendall(msg.encode())
        echo_msg = c.recv(4096)
        print(f"ECHO>> {echo_msg}")
        if msg == "close":
            break
    
    c.close()


if __name__ == "__main__":
    client()