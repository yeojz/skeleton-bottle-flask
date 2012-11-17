"""

 Premise application
 - This is a container framework / micro-CMS for small sites or blog.

 Version: 0.1-alpha

"""
from __future__ import absolute_import
from thirdparty import markdown2
import jinja2
import os


#Variables global
md = markdown2.Markdown()




#Flask based application
from flask import Flask
app = Flask("premise")
app.config.from_object('premise.config')




#Bottle based application
"""
from bottle import Bottle
app = Bottle()
"""



#set all the views file
from . import views 
#from . import api


