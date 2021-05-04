import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction[0]
    eligible = "Congratulations! You are eligible for loan"
    not_eligible = "Sorry! You are not eligible for loan. Please try again later"
    if output == 0:
        return render_template('index.html', prediction_text='{}'.format(eligible))
    else:
        return render_template('index.html', prediction_text='{}'.format(not_eligible))


if __name__ == "__main__":
    app.run(debug=True)