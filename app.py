import os
import bcrypt
from json import loads
from bson.json_util import dumps
#from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request, session, render_template, url_for, flash
from datetime import timedelta
from flask_pymongo import PyMongo
from marshmallow import Schema, fields, ValidationError
from flask_cors import CORS
import bcrypt
import json

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"]= "mongodb+srv://reesespuff:pbcflavor@cluster0.y0ard.mongodb.net/HWVM?retryWrites=true&w=majority"  
mongo = PyMongo(app)

app.secret_key="hansolokillschew"


class machineSchema(Schema):
    Waterusage = fields.Integer(reqiured=True)
    Coins = fields.Integer(reqiured=True)

@app.route("/")
def reh():
    return redirect(url_for('login'))

@app.route("/login", methods=["GET","POST"])
def login():
    
    if request.method == 'POST':
         users = mongo.db.admin
         Admin = users.find_one({'username': request.form['nm']})
         if Admin:
            if request.form['pw'] == Admin['password']:
                session['username'] = request.form['nm']
                flash("Login succesful!")
                return redirect(url_for('home')) 

            else:
                flash("Login unsuccesful")
                return redirect(url_for('login'))

    elif request.method == "GET":
         return render_template('login.html')

@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html')












































if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
