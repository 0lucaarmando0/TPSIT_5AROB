from flask import Blueprint, render_template, request, flash 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')
        #password2 = request.POST.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
            ##elif len(password1) != len(password2):
            ##    flash("Password1 is not equal to password2", category='error') 
        elif len(password1) < 7 :
            flash("Password1 must be greater than 7 characters", category='error')
        else:
            flash("Login success",category='success')
            # Adding to the DB

    return render_template('login.html')





@auth.route('/logout', methods=[ 'GET', 'POST' ])
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=[ 'GET ', 'POST' ])
def sign():
    return render_template('signup.html')
    
