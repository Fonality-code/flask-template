from flask import Flask, redirect, url_for

from config.mongodb import init_db


app = Flask(__name__)



@app.route("/")
def home():
    return "This is the home page"


