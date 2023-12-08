import joblib
from flask import Flask, render_template, request, redirect
import numpy as np
app = Flask(__name__)

print('numpy version:', np.__version__)


@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/PredictCrop')
def predictCrop():
    return render_template('crop.html')

@app.route('/PredictFertilizer')
def predictFertilizer():
    return render_template('fertilizer.html')

@app.route('/PredictCropYeild')
def predictCropYeild():
    return render_template('cropYeild.html')

@app.route('/PredictRainFall')
def predictRainFall():
    return render_template('rainFall.html')

@app.route('/formCrop', methods=["POST"])
def brainCrop():
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosphorus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])
     
    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        joblib.load('crop_app','r')
        model = joblib.load(open('crop_app','rb'))
        arr = [values]
        acc = model.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"


@app.route('/formCropYeild', methods=["POST"])
def brainCropYeild():
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Ph = float(request.form['ph'])
    Rainfall = float(request.form['Rainfall'])

    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

    if Ph > 0 and Ph <= 14 and Temperature < 100 and Humidity > 0:
        joblib.load('crop_app', 'r')
        model = joblib.load(open('crop_app', 'rb'))
        arr = [values]
        acc = model.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"


@app.route('/formFertilizer', methods=["POST"])
def brainFertilizer():
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Ph = float(request.form['ph'])
    Rainfall = float(request.form['Rainfall'])

    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

    if Ph > 0 and Ph <= 14 and Temperature < 100 and Humidity > 0:
        joblib.load('fertilizer_app', 'r')
        model = joblib.load(open('fertilizer_app', 'rb'))
        arr = [values]
        acc = model.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"


@app.route('/formRainfall', methods=["POST"])
def brainRainfall():
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Ph = float(request.form['ph'])
    Rainfall = float(request.form['Rainfall'])

    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

    if Ph > 0 and Ph <= 14 and Temperature < 100 and Humidity > 0:
        joblib.load('crop_app', 'r')
        model = joblib.load(open('crop_app', 'rb'))
        arr = [values]
        acc = model.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"



if __name__ == '__main__':
    app.run(debug=True)















