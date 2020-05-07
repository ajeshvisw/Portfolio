from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/')
def blog(name=None):
	 return render_template('blog.html',name='Ajesh')
@app.route('/blog')
def blog1(name=None):
	return render_template('blog1.html',name='Ajesh')
@app.route('/blogimage')
def blogimage(name=None):
	return render_template('blogimage.html',name='Ajesh')