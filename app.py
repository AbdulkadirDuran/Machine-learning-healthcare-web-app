from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np


app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/heart")
def heart():
    return render_template("heart.html")
@app.route("/documentation")
def documentation():
    return render_template("Heart_Disease_Prediction.html")


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)

    if(int(result)==1):
        prediction = "Sorry! your are suffering from heart disease, please consult a doctor as soon as possible."
    else:
        prediction = "Congrates. Your heart is healthy."
    return(render_template("result.html", prediction_text=prediction))

if __name__ == "__main__":
    app.run(debug=True)
