## 🧠 Student Performance Prediction using Machine Learning

This project uses **Machine Learning** to predict a student’s **final academic performance (G3 grade)** based on various **social, demographic, and study-related factors** such as age, study time, past failures, and attendance.

It aims to help educators **identify at-risk students early** and take **preventive actions** to improve academic outcomes.

---

### 🌐 Live Demo
🎯 **[(https://student-performance-prediction-2-a69n.onrender.com/)]**

---

### 🧩 Features
- Predicts final student grade using an ML model  
- Simple and user-friendly Flask web interface  
- End-to-end ML pipeline: data preprocessing → training → web deployment  
- Hosted online (always accessible) via **Render**

---

### 🏗️ Tech Stack
| Component | Technology |
|------------|-------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask (Python) |
| ML Model | Scikit-learn |
| Deployment | Render |
| Dataset | Student Performance Data (UCI Repository / CSV) |

---

### 🚀 Installation (Run Locally)

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/student-performance-prediction.git
   cd student-performance-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Flask app**
   ```bash
   python app.py
   ```
   App runs locally at:  
   `http://127.0.0.1:5000/`

---

### 📁 Project Structure
```
├── app.py                     # Flask backend
├── student_performance_model.pkl  # Trained ML model
├── templates/
│   └── index.html             # Webpage template
├── static/
│   └── style.css              # Styling (CSS)
├── requirements.txt           # Dependencies
└── Procfile                   # Render deployment config
```

---

### 🧮 Model Training Overview
1. Collected dataset of student academic and personal features.  
2. Preprocessed data (handling missing values, encoding, scaling).  
3. Trained regression/classification model to predict final grade.  
4. Saved trained model as `student_performance_model.pkl`.  
5. Integrated model into Flask app for real-time predictions.

---

### 👨‍💻 Author
**Deepanjan Das**  
**📧 [GitHub Profile link if you want to add]**[(https://github.com/deepanjan23)]

---

### 🏁 License
This project is part of an **IBM SkillBuild Internship Project**.  
For educational and demonstration purposes only.

---

## 📊 Dataset Source
The dataset used for training and testing comes from the  
🎓 **UCI Machine Learning Repository**:  
[Student Performance Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student-mat.csv)

---

## 📸 Screenshots

**1️⃣ Prediction Page (Home)**
![Prediction Page](https://github.com/deepanjan23/Student_Performance_Prediction/blob/main/assets/prediction_page.png)

**2️⃣ Dashboard Page**
![Dashboard Page](https://github.com/deepanjan23/Student_Performance_Prediction/blob/main/assets/dashboard_page.png).

---

## 🤝 Contributions

Contributions are welcome!  
If you'd like to improve the model accuracy or UI design:
1. Fork the repository  
2. Create a new branch  
3. Submit a pull request 🚀  

---

## 💡 Acknowledgment

Developed as part of the **IBM SkillBuild / Internship Project**  
💙 Built with Flask, Machine Learning, and lots of enthusiasm!
=======
# Student_Performance_Prediction
This ML project predicts a student’s final grade (G3) using factors like age, study time, failures, and attendance. Built for an IBM SkillBuild internship, it helps educators identify at-risk students early. It showcases end-to-end ML — from data preprocessing to Flask-based web deployment.
