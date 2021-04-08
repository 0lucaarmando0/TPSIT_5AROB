
from logging import DEBUG
import socket as sock
import sqlite3
from sqlite3.dbapi2 import Cursor
import threading
import logging




ip_serv = "192.168.1.9"
port_serv = 4500

logging.basicConfig(level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s') 


class alphabot_handle(threading.Thread):
    def __init__(self, connection, address ):
        threading.Thread.__init__(self)
        self.conn_tunnel = connection
        self.add = address
        logging.info("Client connected")

    def run(self):
        self.alphabot_receive()


    def alphabot_receive(self):

        logging.info(f"Connection stabilized with : {self.add} ")
        self.choice = self.conn_tunnel.recv(1024).decode()
        self.choice = self.choice.split(",")

        logging.info(f"The message received is : start [{self.choice[1]}], stop [{self.choice[0]}]")
        try:
            self.connection = sqlite3.connect(r"C:\Users\shekh\Desktop\School_Karni\TPSIT\TPSIT_LAB\Alphabot\AlphaBot_Files\Alphabot_Server_side\percorsi.db")
        except:
            logging.error("DB connection not established ")
            
        self.query_creating()

    def query_creating(self):

        cursor = self.connection.cursor()
        #logging.debug(f"SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (SELECT id_start FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_start AND luoghi.nome = '{self.choice[1]}') = inizio_fine.id_start AND(SELECT id_end FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_end AND luoghi.nome = '{self.choice[0]}') = inizio_fine.id_end")
        cursor.execute(f'SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (SELECT id_start FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_start AND luoghi.nome = "{self.choice[1]}") = inizio_fine.id_start AND(SELECT id_end FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_end AND luoghi.nome = "{self.choice[0]}") = inizio_fine.id_end' )
        try:
            self.path = cursor.fetchone()
            if self.path != None:
                logging.info(f"The path to send : {self.path[0]}")
                self.connection.close()
                self.alphabot_sender()
            else:   
                logging.error("Path not found , error in the input. ")
        except:
            logging.error("Something went wrong in the cursor")
        
        
            
        
    def alphabot_sender(self):

        self.conn_tunnel.sendall(self.path[0].encode())
        
        


def main():
    
    try:
        serv = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        serv.bind((ip_serv, port_serv))
        serv.listen()

        while True:
            conn, add = serv.accept()
            alphabot = alphabot_handle(conn, add)
            alphabot.start()

    except:
        logging.error("Failed to start the server ")



if __name__ == "__main__":
    main()