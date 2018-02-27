# coding:utf8

from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blue_print
from app.admin import admin as admin_blue_print

app.register_blueprint(home_blue_print)
app.register_blueprint(admin_blue_print, url_prefix="/admin")
