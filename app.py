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

        raw = request.get_data()
        data = request.json
        # print b

        try:
            usr_id = data['message']['chat']['id']
            text = data['message']['text']
        except:
            text=" "

        data_new = ""
        dic = text.split(' ')
        for i in dic:
            if len(i) >= 5:
                print i
                val = random.randint(0,1)
                print api_keys[val]

                new_url = "http://words.bighugelabs.com/api/2/"+str(api_keys[val])+"/"+i+"/json"
                c = requests.get(new_url)

                if c.status_code == 200:
                    result = c.json()
                    print result
                    

    elif request.method == "GET":
        print "error"



    return "HI"






if __name__ == '__main__' :
	# port = int(os.environ.get('PORT',443))
	# app.run(host='0.0.0.0',port=port)
	app.run(debug=True)
