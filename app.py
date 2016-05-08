from flask import Flask
from flask import render_template,request,flash,url_for,redirect,session
import requests
import os,json
import random


app = Flask(__name__)
app.secret_key = "secret"

api_keys = ['d687a4bbd8b4a787b2f8c841db313763','806706827f427b6a77ff242b936ae973','9667ebccf1c18f24c76263a34352ca07','ef933fa89506062e98ba214165fdad5f','aba132076d484dcf8d0a69a299561c8e']


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
    print st
    return st

@app.route('/api', methods=['GET','POST'])
def main():

    if request.method == 'POST':
        print "POSTED"

        raw = request.get_data()
        data = request.json
        print data

        try:
            usr_id = data['message']['chat']['id']
            text = data['message']['text']
            if text.find("\U0001") == -1:   #added to ignore stickers
                text = data['message']['text']
            else:
                text = 'no'                   #random single character as it ignores it
        except:
            text=" "

        print text
        data_new = ""
        dic = text.split(' ')
        for i in dic:
            if len(i) >= 5:
                print i
                val = random.randint(0,4)
                print api_keys[val]

                new_url = "http://words.bighugelabs.com/api/2/"+str(api_keys[val])+"/"+i+"/json"
                c = requests.get(new_url)
                print  c.status_code

                if c.status_code == 200:

                    result = c.json()
                    print result
                    txt = process(result,i)
                    data_new =  data_new + txt

        print data_new
        if data_new  != "":
            url = "https://api.telegram.org/bot183846920:AAG8aKPDPoKwgNuMomNCTKm6D-FTi9L0NLI/sendMessage?chat_id=" + str(usr_id) + "&parse_mode=markdown&text="+data_new+""
            e = requests.get(url)


    elif request.method == "GET":
        print "error"



    return "HI"






if __name__ == '__main__' :
	port = int(os.environ.get('PORT',443))
	app.run(host='0.0.0.0',port=port)
	# app.run(debug=True)
