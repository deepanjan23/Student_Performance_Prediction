# 🎓 Student Performance Prediction (IBM Project)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-ScikitLearn-orange)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap5-lightblue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📘 Project Overview

**Student Performance Prediction** is a machine learning web application that predicts a student’s **final grade (G3)** based on academic and behavioral attributes such as study time, past failures, and absences.

The goal of this IBM project is to help institutions identify underperforming students early and implement personalized interventions to improve their academic success.

---

## 🚀 Key Features

- 📊 Predicts final student grades (G3) using regression models  
- 🧠 Classifies students as Pass/Fail based on predicted score  
- 💻 Flask web app for interactive user input and prediction  
- 🎨 Modern, responsive UI using Bootstrap 5  
- 📈 Dashboard visualizations (Chart.js):
  - Study Time vs Final Grade  
  - Absences vs Final Grade  
- ☁️ Deployable on IBM Cloud / Watson Studio  

---

## 🧩 Tech Stack

| Category | Technology Used |
|-----------|------------------|
| **Language** | Python 3 |
| **Libraries** | Pandas, NumPy, Scikit-learn, Joblib |
| **Visualization** | Matplotlib, Seaborn, Chart.js |
| **Web Framework** | Flask |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Deployment** | IBM Cloud / Localhost |

---

## 🗂️ Project Structure

```
Student_Performance_Prediction/
│
├── app.py                        # Flask backend
├── student_performance_model.pkl  # Trained ML model
├── student-mat.csv                # Dataset (UCI)
├── templates/
│   ├── index.html                 # Main prediction page
│   └── dashboard.html             # Visualization dashboard
├── static/                        # Optional static files (CSS, JS)
└── README.md                      # Project documentation
```

---

## 🧠 Machine Learning Workflow

1. **Data Collection:** UCI Student Performance dataset  
2. **Preprocessing:** Cleaning & selecting relevant features  
3. **Model Training:** Linear Regression / Random Forest  
4. **Evaluation:** Using R² Score and Accuracy metrics  
5. **Deployment:** Flask app for live predictions  

---

## ⚙️ How to Run Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/student-performance-prediction.git
cd student-performance-prediction
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Flask App
```bash
python app.py
```

Then open your browser and visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Dataset Source
The dataset used for training and testing comes from the  
🎓 **UCI Machine Learning Repository**:  
[Student Performance Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-mat.csv)

---

## 📸 Screenshots

**1️⃣ Prediction Page (Home)**
![Prediction Page](https://github.com/your-username/student-performance-prediction/assets/demo1.png)

**2️⃣ Dashboard Page**
![Dashboard Page](https://github.com/your-username/student-performance-prediction/assets/demo2.png)

---

## 🤝 Contributions

Contributions are welcome!  
If you'd like to improve the model accuracy or UI design:
1. Fork the repository  
2. Create a new branch  
3. Submit a pull request 🚀  

---

## 🧾 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it with attribution.

---

## 💡 Acknowledgment

Developed as part of the **IBM SkillBuild / Internship Project**  
💙 Built with Flask, Machine Learning, and lots of enthusiasm!
