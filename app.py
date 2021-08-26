import numpy as np
import pandas as pd
import pickle
from flask import  Flask, render_template, url_for, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__, template_folder="template")
model = pickle.load(open("churn.pkl", "rb"))
st = pd.read_csv("CChurn.csv")

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return render_template("index.html")


@app.route('/predict', methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method ==  'POST':
        CreditScore = request.form['CreditScore']
        Geography = request.form['Geography']
        Gender = request.form['Gender']
        Age = request.form['Age']
        Tenure = request.form['Tenure']
        Balance = (request.form['Balance'])
        NumOfProducts = request.form['NumOfProducts']
        HasCrCard = (request.form['HasCrCard'])
        IsActiveMember = (request.form['IsActiveMember'])
        EstimatedSalary = (request.form['EstimatedSalary'])


        if (Geography == "France"):
            Geography=0
        elif (Gender == "Spain"):
            Geography=1
        else:
            Geography=2

        if (Gender == "Female"):
             Gender = 0
        else:
             Gender = 1
        
        if (HasCrCard == "no"):
             HasCrCard = 0
        else:
             HasCrCard = 1

        if (IsActiveMember == "no"):
             IsActiveMember = 0
        else:
             IsActiveMember = 1

        
        input = [[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]]
        prediction = model.predict(input)
        print(prediction)


        if(prediction== 0):
            prediction="The customer is happy with the membership and might not leave!!!"
        else:
            prediction="The customer is not very much pleased with the services, He might close his account!!"

        return render_template('index.html', prediction_text = 'Your Result is : {}'.format(prediction))
        
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)