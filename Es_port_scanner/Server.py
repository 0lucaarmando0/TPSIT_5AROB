import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "127.0.0.1"
port = 7000

address = (ip, port)

def main():
    s.bind(address)

if __name__ == "__main__":
    main()