from flask import Flask, request, jsonify, render_template, make_response
from flask import send_file
import os

app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/map")
def map():
    return render_template('cal_housing.html')

@app.route("/attr")
def attr():
    return render_template('attr.html')

@app.route("/featcorr")
def fc():
    return render_template('featcorr.html')






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)


