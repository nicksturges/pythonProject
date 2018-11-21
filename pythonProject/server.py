from flask import Flask, render_template, redirect, session, request, flash
# from flask_bcrypt import Bcrypt   
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# from mysqlconnection import connectToMySQL
app=Flask(__name__)
# bcrypt = Bcrypt(app)
# app.secret_key= 'jodomcase'
# mysql = connectToMySQL('reg_login2')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def reg():
    return render_template('register.html')



@app.route('/profiles')
def profiles():
    return render_template('ranger_profile.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug = True)
   