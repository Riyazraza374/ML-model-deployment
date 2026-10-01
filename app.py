from flask import Flask, render_template, request, jsonify
from utils import model_predict
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form.get('content')
    predictions = model_predict(email_text)
    return render_template('index.html', email_text=email_text, predictions=predictions)

@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email = data['content']
    predictions = model_predict(email)
    return jsonify({'prediction': predictions, 'email': email})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)