from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load your trained ML model
model = joblib.load("student_performance_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert input values from form to float
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])[0]
        return render_template('index.html', prediction_text=f'Predicted Final Grade: {prediction}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    # Run the app on Render
    app.run(host='0.0.0.0', port=5000)
