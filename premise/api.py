from __future__ import absolute_import
from . import app, md

#List of APIs
@app.route("/api")
@app.route("/api/<option>")    
def api(option=""):

	return "API" 
