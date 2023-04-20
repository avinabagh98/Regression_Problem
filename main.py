from flask import Flask,render_template,request
import pickle
import numpy as n

app = Flask(__name__)
model = pickle.load(open('knn_reg_pckl_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home2.html')


@app.route('/predict', methods = ['POST'])


def predict():
    holiday = int(request.form.get('holiday'))
    workingday= int(request.form.get('workingday'))
    weather = int(request.form.get('weather'))
    atemp= int(request.form.get('atemp'))
    humidity= int(request.form.get('humidity'))
    windspeed= int(request.form.get('windspeed'))
    hour= int(request.form.get('hour'))
    day = int(request.form.get('day'))
    month= int(request.form.get('month'))
    year= int(request.form.get('year'))

    result = model.predict([[holiday, workingday, weather, atemp, humidity, windspeed, hour, day, month, year]])

    return render_template('home2.html', value=result)


if __name__ == "__main__":
    app.run(debug = True)