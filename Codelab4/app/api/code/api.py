from flask import Flask,render_template,jsonify,request
import json
import random
import os

app = Flask(__name__)
 
food = {"pizza" : 5, "chocolate": 4, "dosa" : 1, "croissant":2,"Amortentia":20 , "Polyjuice":12 , "Felix Felicis":43 , "Skele-Gro": 22,
"Wolfsbane":12, "Veritaserum":14 , "Jawbind": 20 , "Quodpot" : 25}

food_list=list(food)

@app.route('/')
def landingpage():
    return render_template('index.html')

@app.route("/api/food",methods = ['GET'])
def food_dictionary():
    return jsonify({"food":food})

@app.route('/api/random',methods= ['GET'])
def randres():
    res = key, val = random.choice(list(food.items()))
    return jsonify({"Food: ": key, "Price ($): ": val})
    #    key1=random.choice(list(food))
    #    return str(key1) + ':' + str(food[key1])

@app.route('/api/addmeal',methods=['POST'])
def addMeal():
    newMeal = {'meal':request.json['meal']}
    food.append(newMeal)
    return jsonify({'food': food })
       
if __name__ == "__main__":
    #  app.run('0.0.0.0', port=5000,debug=True)
    port=os.environ.get('API_PORT')
    app.run('0.0.0.0',port=port,debug=True)

