# This is a sample Python script.
from flask import Flask, render_template
from config import Configuration
from time import time, asctime
from pymongo import MongoClient
from flask_pymongo import PyMongo
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)
app.config.from_object(Configuration)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
print('hop 12')
myclient = MongoClient("mongodb://db:27017/")
print('hop14')
#mydb = myclient["citizens_database"]
mydb = myclient.citizens_database
print('hop17')
import sys



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
