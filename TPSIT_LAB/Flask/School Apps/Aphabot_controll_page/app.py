#########################################################################
#                                                                       #
# Author: Karni Singh Shekhawat                                         #
# Date: 07/02/2021                                                      #
# Description: This is a web server for the Alphabot controller page    #
#                                                                       #
#########################################################################

from flask import Flask, render_template, request, url_for
import logging
from time import sleep
# importing Alphabot form the Alphabot Class
#from Alphabot import AlphaBot

# Setting up the logging module
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# Setting up the app 
app = Flask(__name__)

# Setting up an Alphabot runner
#ap = AlphaBot()

# Setting up the mail page load
@app.route('/')
def index():
    return render_template('index.html')

# Setting up the forward runner
@app.route('/forward')
def forward():
    logging.debug('Forwarding')
    #ap.forward()
    sleep(1)
    return render_template('index.html')

# Setting up the backward runner
@app.route('/backward')
def backward():
    logging.debug('Going backward')
    #ap.backward()
    sleep(1)
    return render_template('index.html')

# Setting up the left turn
@app.route('/left')
def left():
    logging.debug('Turning left')
    #ap.left()
    sleep(1)
    return render_template('index.html')

# Setting up the right turn
@app.route('/right')
def right():
    logging.debug('Turning right')
    #ap.right()
    sleep(1)
    return render_template('index.html')




# Setting up the main runner 
if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
