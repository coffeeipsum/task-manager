import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://admin:1Diploma1Diploma@ds255260.mlab.com:55260/task_manager'


mongo = PyMongo(app) #that's called a Constructor Method

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", 
    tasks=mongo.db.tasks.find())


# @app.route('/')
# def hello():
#     return "Hello World ...again"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)