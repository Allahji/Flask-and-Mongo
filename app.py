# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]

# name of database
app.config['MONGO_DBNAME'] = 'database1'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:hys3U6eF4yYpIN7c@cluster0.0bu5m.mongodb.net/database1?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    user = mongo.db.users

    # insert new data
    user.insert({"name": "allahji"})

    # return a message to the user
    return "Added a new user"

@app.route('/event')
def event():
    joy = mongo.db.users
    users = joy.find({"name" : "allahji"})
    return render_template("event.html", users = users)