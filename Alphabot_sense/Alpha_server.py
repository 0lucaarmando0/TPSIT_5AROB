from flask import Flask, jsonify, request
import sqlite3 as sql
import logging


#logger settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)


# DB Setting up 
try:
    db = sqlite3('')
    cursore = db.cursor()
except : 
    logging.error("Database error")

@app.route('/sersor')
def sersorInfo():

    DR = request.args.get('DR')
    DL = request.args.get('DL')
    time = request.args.get('time')
    date = request.args.get('date')

    try:
        cursore.execute(f"INSERT INTO ")
    except:
        logger.error("Execution query failed")

@app.route('/')
def index():
    return "TODO"
    

if __name__ == "__main__":
    app.run(debug=True)
