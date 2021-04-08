
import socket as sok
import turtle
import logging
from time import sleep
import re
# importing the Alphabot moving class
from Alphabot import AlphaBot

# global variables setting 
server_ip = "192.168.1.9"
server_port = 4500
full_address = (server_ip, server_port)

# Insistence of Alphabot class
ap = AlphaBot()
    

# Setting up the loggers 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s') 


# Setting up the socket 
def set_socket():
    client = sok.socket(sok.AF_INET, sok.SOCK_STREAM)
    client.connect(full_address)
    
    #client.recv()

    return client


# Sending the request for the path 
def request_send(client):
    print("Input the [stop,start] for the path:")
    request_path = input('>>')

    try:
        logging.debug(request_path)
        # the request sent 
        client.sendall(request_path.encode())
    except:
        logging.exception("Request was not made")


# Receiving form the server
def receiving_path(client):

    try:
        answer = client.recv(1024)
        print(answer)
        answer = answer.decode()
        answer = answer.strip('][').split(', ')
        print(answer)
        answer = answer[0]
        print(answer) 

        return answer 

    except:
        logging.exception("Something went wrong with receiving the path")


def answer_check(answer):

    if re.findall("^0", answer):
        # Server error produce 
        logging.debug("The server has given an error :")
        logging.debug(answer)
    else:
        # We received the path (F100 L90 F500 R45 F200 R45 B100)
        semi_path = re.findall(r'(\w+?)(\d+)', answer)
        logging.debug(semi_path)
        print(type(semi_path))
        path = {} 
        for elements in semi_path:
            #Making the path more readable 
            elements = str(elements)
            elements = elements.replace('(','').replace(')','').replace("'",'').replace(',','')
            tempo_path = elements.split(' ')
            
            logging.debug(elements)
            
            path.update({tempo_path[0]: int(tempo_path[1])})
        
        logging.info(path)
        
        return path
        
    

def movieAlphabot(path):

    for key in path:
        if key == "F":
            print("Forward")
            ap.forward()
            sleep(path.get(key, None)/100)
            ap.stop()
            
        
        elif key == "B":
            print("Backward")
            
            ap.backward()
            sleep(path.get(key, None)/100)
            ap.stop()
            

        elif key == "R":
            print("Right")
            
            ap.right()
            sleep(path.get(key, None)/100)
            ap.stop()
            
            
        elif key == "L":
            print("Left")
            
            ap.left()
            sleep(path.get(key, None)/100)
            ap.stop()
            

        else:
            pass
            logging.info("The path has some kind of problem in the key : {key}")


def main():
    
    client = set_socket()
    request_send(client)
    
    answer = receiving_path(client)

    commands = answer_check(answer)

    # Using the path for moving the Alphabot
    movieAlphabot(commands)



if __name__ == "__main__":
    main()
