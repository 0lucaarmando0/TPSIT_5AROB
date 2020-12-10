import socket
import threading

server_ip = "192.168.1.5"
server_port = 7000

def client():
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect((server_ip,server_port))

    while True:
        msg = input("Inserire info1 e info2 separati da una virgola: ") #Invio della tupla
        msg_request = msg.split(",")

        tupla = (msg_request[0], msg_request[1])
        print(tupla)
        c.sendall(str(tupla).encode())
        answer_msg = c.recv(4096)
        print(f"answer: {answer_msg}")
        if msg == "close":
            break
    
    c.close()


if __name__ == "__main__":
    client()