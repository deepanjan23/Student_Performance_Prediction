from flask import Flask, request, render_template
import joblib
import numpy as np
from pyngrok import ngrok, conf
import webbrowser
import threading
import time

app = Flask(__name__)

# Load your trained ML model
model = joblib.load("student_performance_model.pkl")

@app.after_request
def skip_ngrok_warning(response):
    response.headers["ngrok-skip-browser-warning"] = "true"
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])[0]
        return render_template('index.html', prediction_text=f'Predicted Final Grade: {prediction}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

def start_ngrok():
    # ✅ Add your ngrok auth token here
    conf.get_default().auth_token = "35LOsieLr7om6k32Ij4L82ITMiA_6X8UsWA2S4CW8yMCWfPtF"

    # Create the tunnel
    url = ngrok.connect(5000).public_url
    print(f"🌐 Public URL: {url}")
    webbrowser.open(url)
    
    # Keep tunnel alive
    while True:
        time.sleep(3600)

if __name__ == "__main__":
    # Start ngrok in background
    threading.Thread(target=start_ngrok, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
