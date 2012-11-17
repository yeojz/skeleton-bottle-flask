from __future__ import absolute_import

from . import app, md
from .shared import requireLogin

from flask import render_template








"""
Main
"""



@app.route("/")
def home():
	return render_template('index.html')


    
	

@app.route("/md")
def home():
	print md.convert("*boo!*")
	return