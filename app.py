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
	loadmore=True
	count=1
	stores_list = query_all()
	stores=[]
	print("-------------------------" + str(len(stores_list)))
	if(len(stores_list)<12):
		stores=stores_list
	else:
		for i in range(count*12):
			stores.append(stores_list[i])
	print(stores_list)
	next_count=count+1
	if (len(stores_list)<(next_count*12)):
		loadmore=False
	return render_template('home.html', stores=stores,next_count=next_count,loadmore=loadmore)

@app.route('/<int:count>',methods=['GET','POST'])
def home_loaded(count):
	loadmore=True
	stores_list = query_all()
	stores=[]

	if(len(stores_list)<12*count):
		stores=stores_list
	else:
		for i in range(count*12):
			stores.append(stores_list[i])

	if(count == (((len(stores_list)%12)+(len(stores_list))/12))):
		stores=stores_list

	elif (len(stores_list)%12 == 0):
		for i in range(count*12):
			j=12
			stores.append(stores_list[i+j])
			j = j * 2

	next_count=count+1
	if (len(stores_list)<(count*12)):
		loadmore=False
		print(len(stores_list))
		print(len(stores))
	return render_template('home.html', stores=stores,next_count=next_count,loadmore=loadmore)
	
@app.route('/addStore', methods=['POST'])
def addStore():
	#if sha256(request.form['pass'].decode()).hexdigest() == pass_hash:
	if request.method == "POST":
		add_store(request.form['name'], request.form['city'], request.form['street'], request.form['phone'])
		return home()

	else:
		return 'Invalid password <br> <a href="/">Home</a>'

if __name__ == '__main__':
	app.run(debug=True)