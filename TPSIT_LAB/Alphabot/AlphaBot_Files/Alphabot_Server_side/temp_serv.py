import socket as sock
from time import sleep

ip_serv = "192.168.1.9"
port_serv = 4500
fulladdress=(ip_serv,port_serv)

serv = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
serv.bind(fulladdress)
serv.listen()
conn, add = serv.accept()
print(f"The connection  : {conn}")

massagge = conn.recv(1024)

print(massagge)
mass_path =  str([0,"F800R90B800L90"])
conn.sendall(mass_path.encode())



sleep(8000) 
