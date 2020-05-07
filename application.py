from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/')
def home(name=None):
	return render_template('application.html',name='Ajesh')
@app.route('/news')
def news(name=None):
	return render_template('news.html',name='Ajesh')
@app.route('/about')
def about(name=None):
	return render_template('about.html',name='Ajesh')
@app.route('/pro')
def pro(name=None):
	return render_template('pro.html',name='Ajesh')