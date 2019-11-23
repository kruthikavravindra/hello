import flask
from flask import request, jsonify
import face_recognition
import numpy as np
import glob
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/resources/books/home', methods=['GET'])
def home():
    return 'okk'
    print("hi")
    
# # A route to return all of the available entries in our catalog.
# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def home1():
    # we=home()
    # return "we"

app.run()