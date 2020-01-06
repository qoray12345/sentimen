import pickle
import pandas
from sklearn import model_selection
#from sklearn.linear_model import LinearRegression
import json
from flask import Flask, request
from flask_cors import CORS
import sys
import re

filename = 'yeheyyy.sav'
loaded_model = pickle.load(open(filename, 'rb'))
# print(loaded_model)
app = Flask(__name__) 
CORS(app)

@app.route('/example', methods=['POST'])
def sentiment():
    req_data = request.get_json()
    # inputt =['Berikut perkembangan kebakaran hutan dan lahan (karhutla) tiap hari ya.. Keliatan kan ada progressnya?  pic.twitter.com/hpUJmNJ9kk',
    # 'Berikut perkembangan kebakaran hutan dan lahan (karhutla) tiap hari ya.. Keliatan kan ada progressnya?  pic.twitter.com/hpUJmNJ9kk',
    # 'Berikut perkembangan kebakaran hutan dan lahan (karhutla) tiap hari ya.. Keliatan kan ada progressnya?  pic.twitter.com/hpUJmNJ9kk',
    # 'Berikut perkembangan kebakaran hutan dan lahan (karhutla) tiap hari ya.. Keliatan kan ada progressnya?  pic.twitter.com/hpUJmNJ9kk',
    # 'Berikut perkembangan kebakaran hutan dan lahan (karhutla) tiap hari ya.. Keliatan kan ada progressnya?  pic.twitter.com/hpUJmNJ9kk']
    inputt = req_data['data']
    print(inputt[0])
    input = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([0-9])','', inputt[0])
    res = loaded_model.predict(inputt)
    sentimen = []
    score = []

    for a in res:
        if a == 0:
            sentimen.append('negatif')
        if a == 1:
            sentimen.append('netral')
        if a == 2:
            sentimen.append('positif')

    hasil = []

    if len(sentimen) == len(inputt):
        for f, b in zip(inputt, sentimen):
            sentimen =  {
                'OriginalText' : f,
                'sentimen' : b,
                # 'socre' : loaded_model.score(f)
            }
            hasil.append(sentimen)

    send = {
            'status' :True,
            'message' : 'success',
            'data'  : hasil
        }
        
    # print(json.dumps(send))
    return json.dumps(send)
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2],threaded=True, debug=False)