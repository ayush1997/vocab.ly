from flask import Flask
from flask import render_template,request,flash,url_for,redirect,session
import requests
import os,json
import random


app = Flask(__name__)
app.secret_key = "secret"

api_keys = ['0c209d14061fe2f68b64e9dfd9453280','88044ee383eef5827ee87f3022224354']


@app.route('/api', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        print "POSTED"

        raw_data = request.get_data()
        data = request.json
        # print b

    elif request.method == "GET":
        print "error"



    return "HI"






if __name__ == '__main__' :
	# port = int(os.environ.get('PORT',443))
	# app.run(host='0.0.0.0',port=port)
	app.run(debug=True)
