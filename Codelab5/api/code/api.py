from random import randint
from flask import Flask, jsonify
import json
import os
from sqlalchemy import create_engine
#import psycopg2

app = Flask(__name__)

db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('PG_USER')
db_pass = os.environ.get('PG_PASS')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('PG_PORT') 

fetched_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
fetched_db = create_engine(fetched_string)

def fetch_surprise():
    query = "SELECT foodName, price FROM Menu ORDER BY RANDOM() LIMIT 1;"
    records = fetched_db.execute(query)
    surprise_meal = []
    for r in records:
        temp = (r[0], r[1])
        surprise_meal.append(temp)
    return list(surprise_meal)

@app.route('/')
@app.route('/surprise/')
def index():
   return jsonify(fetch_surprise())
app.run(host='0.0.0.0', port=os.environ.get('API_PORT'))

#@app.route('/')
#def fetch_surprise():
    #conn = psycopg2.connect(db_name=os.environ.get('DB_NAME'),
    #                        db_user=os.environ.get('PG_USER'),
    #                        db_pass=os.environ.get('PG_PASS'),
    #                        db_host=os.environ.get('DB_HOST'),
    #                        db_port=os.environ.get('PG_PORT'))
    #cursor = conn.cursor()
    #cursor.execute("SELECT foodName, price FROM Menu ORDER BY RANDOM() LIMIT 1;")
    #result = cursor.fetchall()
    #conn.close()
    #rec = {"Meal": result[0][0], "Price": str(result[0][1])}
    #return json.dumps(rec)
#if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=os.environ.get("API_PORT"))