from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# load model
LABEL = ['Tidak ada Kegagalan','Terjadi Kegagalan']
with open("model_rf.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "<h1> Model Prediksi Kegagalan Alat </h1>"

@app.route("/predict", methods=["GET", "POST"])
def predict_failure():
    if request.method == "POST":
        content = request.json
        try:
            new_data = {'Process temperature [K]': content['suhu_proses'],
                        'Rotational speed [rpm]': content['kecepatan_rotasi'],
                        'Torque [Nm]': content['torsi'],
                        'Tool wear [min]': content['lama_penggunaan']}
            new_data = pd.DataFrame([new_data])
            res = model.predict(new_data)
            result = {'class': str(res[0]),
                        'class_name': LABEL[res[0]]}
            response = jsonify(success= True,
                                result = result)
            return response, 200
        except Exception as e:
            response = jsonify(success= True,
                               message=str(e))
            return response, 400
    # return dari method get
    return "<p>Silahkan gunakan method POST untuk mode <em>inference model</em></p>"

#app.run(debug=True)