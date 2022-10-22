from flask import Flask, render_template
import os
import json
from urllib.request import urlopen 

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def fetch_meal_surprise():
    db_url = "http://{api_host}:{api_port}/surprise/".format(api_host = os.environ.get("API_HOST"),
                                                             api_port = os.environ.get("API_PORT"))
    response1 = urlopen(db_url)
    response2 = response1.read()
    response3 = json.loads(response2)
    return render_template('index.html', meal=response3[0][0], price=response3[0][1])
app.run(host='0.0.0.0', port=os.environ.get("CONSUMER_PORT"))
