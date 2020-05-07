from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/')
def pro(name=None):
	return render_template('pro.html',name='Ajesh')