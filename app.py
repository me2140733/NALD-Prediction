from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Total Stops
        Age = int(request.form["Age"])
        Sex = int(request.form["Sex"])
        eGFR = int(request.form["eGFR(mL/min/1.73 m^2)"])
        Hypoalbuminemia = int(request.form["Hypoalbuminemia"])
        Duration = (int(request.form["Expected surgical Duration(hours)"]))*5
        Emergency = int(request.form["emergency operation"])
        Diabetes = int(request.form["Diabetes"])
        RAAS = int(request.form["RAAS Blockade Use"])
        Anemia = int(request.form["Anemia"])
        Hyponatremia = int(request.form["Hyponatremia"])
        # print(Total_stops)
        
        score = Age + Sex + eGFR + Hypoalbuminemia + Duration + Emergency + Diabetes + RAAS + Anemia + Hyponatremia

        if(score<20):

            return render_template('home.html',prediction_text="This patient has AKI risk < 2% and critical AKI risk < 2%")
        if(20<=score<=39):

            return render_template('home.html',prediction_text="This patient has AKI risk >= 2% and critical AKI risk < 2%")
        if(40<=score<=59):

            return render_template('home.html',prediction_text="This patient has AKI risk >= 10% and critical AKI risk >= 2%")
        if(score>=60):

            return render_template('home.html',prediction_text="This patient has AKI risk >= 20% and critical AKI risk >= 10%")


    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)
