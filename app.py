from flask import Flask
from flask import render_template,request,flash,url_for,redirect,session
import requests
import os,json
import random


app = Flask(__name__)
app.secret_key = "secret"

api_keys = ['3dd7504f5e429ecd23ad7d5fb908f1ac','3738b8451482552cf1a88378c4bef15f']


def process(result,word):
    st = ""
    key = result.keys()
    print key
    l = len(key)

    for i in range(l):
        try:
            f = result[key[i]]['syn']
        except:
            try:
                f = result[key[i]]['sim']
            except:
                f = ["Not gettng anhing"]
        print f

        st = st +" "+ key[i].upper()+": "
        print st

        if len(f) > 5:
            for k in range(5):
                st = st+" "+f[k]
        else:
            for j in f:
                st = st+" "+j

    st = "*" + word+ "*" + "```" + st + "```"
    return st

@app.route('/api', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        print "POSTED"

        raw = request.get_data()
        data = request.json
        print b

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
                    txt = process(result,i)
                    data =  data + txt

        if data  != "":
            url = "https://api.telegram.org/bot183846920:AAGxGTDQXECbBOVDXRa6DLvssQ_MPucDERs/sendMessage?chat_id=" + str(usr_id) + "&parse_mode=markdown&text="+data+""
            requests.get(url)
    elif request.method == "GET":
        print "error"



    return "HI"






if __name__ == '__main__' :
	# port = int(os.environ.get('PORT',443))
	# app.run(host='0.0.0.0',port=port)
	app.run(debug=True)
