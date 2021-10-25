from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import joblib

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
        Gender = int(request.form["Gender"])
        Total_Bilirubin = float(request.form["Total Bilirubin"])
        Direct_Bilirubin = float(request.form["Direct Bilirubin"])
        Alkaline_Phosphotase = float(request.form["Alkaline Phosphotase"])
        Alamine_Aminotransferase = float(request.form["Alamine Aminotransferase"])
        Aspartate_Aminotransferase = float(request.form["Aspartate Aminotransferase"])
        Total_Protiens = float(request.form["Total Protiens"])
        Albumin = float(request.form["Albumin"])
        Albumin_and_Globulin_Ratio = float(request.form["Albumin and Globulin Ratio"])
        # print(Total_stops)
        loaded_model = joblib.load('LiverDisease.pkl', mmap_mode=None)
        data= [[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,
               Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]]
        dftest = pd.DataFrame(data, columns = ['Age','Gender','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase',
                                               'Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Albumin_and_Globulin_Ratio'])                           
        result = loaded_model.predict(dftest)
                             
        

   

        if(result[0]==1):

            return render_template('home.html',prediction_text="This patient may have liver disease")
        if(result[0]==0):

            return render_template('home.html',prediction_text="This patient may not have liver disease")


    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)
