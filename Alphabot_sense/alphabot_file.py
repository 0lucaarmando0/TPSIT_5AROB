import requests
import logging
from datetime import datetime
from alphabot import Alphabot
from RPi.GPIO import GPIO

DR = 16 #pin's number on raspberry Pi
DL = 19 #pin's number on raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP) #set DR as input
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP) #set DL as input

# Time stamp
current_day = datetime.Today()
current_time = datetime.strptime("%H:%M")

# Alphabot Settings
bot = Alphabot()

# Settings up logging
logging.basicConfig(level=Debug, format='%(asctime)s:%(levelname)s:%(message)s')



def info_setup(DL_status, DR_status):
    url = "http://127.0.0.1:5000/sensor"
    params = {"DR": DR_status, 'DL' : DL_status, "day" : current_day, 'time' : current_time}
    try:
        r = requests.get(url = url, params = params)
        print(r.status())
    except : 
        logging.error("requests error")

def sensorReader():
    try:

        while True:
            DR_status = GPIO.status(DR)
            DL_status = GPIO.status(DL)


            if(DL_status == 1 and DR_status == 1): 
                # Nothing in the path
                bot.forward()
            elif(DL_status == 1 and DR_status == 0):
                # Something on the right side
                bot.left()
            elif(DL_status == 0 and DR_status == 1):
                # Something on the left side               
                bot.right()
            else:
                # Something infront of us 
                bot.backward()
    except : 
        bot.stop()
        logger.error("status error")


if __name__ == "__main__":
    bot.stop()
    sensorReader()