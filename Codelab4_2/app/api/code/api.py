from flask import Flask,render_template,jsonify,request
import json
import random
import os

app = Flask(__name__)
 
food = {"Gulab Jamun":5, "Chicken Tikka":4, "dosa":1, "Pizza":2,"Amortentia":20,
"Spaghetti":12, "Love Potion":43 , "Alfred's special dish":22, "Penny's wrong order":12,
"Cheesecake":14, "Dark Chocolate Mocha":20, "Salad":25}

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

@app.route('/api/addmeal',methods=['POST'])
def addMeal():
    newMeal = {'meal':request.json['meal']}
    food.append(newMeal)
    return jsonify({'food': food })
       
if __name__ == "__main__":
    port=os.environ.get('API_PORT')
    app.run('0.0.0.0',port=port,debug=True)

