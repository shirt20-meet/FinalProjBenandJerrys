from database import *
import os
from flask import Flask, request, redirect, render_template, url_for
from flask import session as login_session
from werkzeug import secure_filename
from hashlib import sha256

app = Flask(__name__)

pass_hash = '530a6928a38a2a2de00e4e6c7d5465996f9d501efa44efa7adacc9a2e8569ac1'

app.config['SECRET_KEY'] = 'shir-tale-aboud-maayan'

@app.route('/')
def home():
    stores = query_all()
    return render_template('home.html', stores=stores)
    
@app.route('/addStore', methods=['POST'])
def addStore():
    if sha256(request.form['pass'].decode()).hexdigest() == pass_hash:
        add_store(request.form['name'], request.form['address'], request.form['phone'])
        return home()

    else:
        return 'Invalid password <br> <a href="/">Home</a>'

if __name__ == '__main__':
    app.run(debug=True)