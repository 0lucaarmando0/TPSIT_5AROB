from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        name = request.form["username"]
        mail = request.form["email"]
        psw = request.form["password"]
        psw = hashlib.md5(psw.encode())
        
    
    return render_template("register.html", name= name, email=mail, password=psw)
    



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8084, debug=True)