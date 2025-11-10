from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load saved model
model = joblib.load("student_performance_model.pkl")

# Load or simulate some student data for visualization
try:
    df = pd.read_csv("student-mat.csv", sep=';')
except FileNotFoundError:
    # If dataset not available, create dummy data for charts
    data = {
        'studytime': np.random.randint(1, 5, 50),
        'absences': np.random.randint(0, 20, 50),
        'G1': np.random.randint(5, 20, 50),
        'G2': np.random.randint(5, 20, 50),
        'G3': np.random.randint(5, 20, 50)
    }
    df = pd.DataFrame(data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text=f'Predicted Final Grade: {round(prediction[0], 2)}')

@app.route('/dashboard')
def dashboard():
    # Prepare data for charts
    studytime = df['studytime'].tolist()
    absences = df['absences'].tolist()
    g3 = df['G3'].tolist()

    return render_template('dashboard.html',
                           studytime=studytime,
                           absences=absences,
                           g3=g3)

if __name__ == "__main__":
    app.run(debug=True)
