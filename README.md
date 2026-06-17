#  IntelliHire AI – Smart Internship Candidate Screening System

An AI-powered Machine Learning web application developed to automate the internship candidate screening process. The system intelligently evaluates candidate profiles and predicts their suitability for internship opportunities using multiple Machine Learning algorithms.

---

##  Project Overview

IntelliHire AI is designed to simplify and automate the initial candidate screening process followed by organizations during internship recruitment.

The application analyzes multiple candidate attributes and provides intelligent recommendations based on machine learning predictions. It also categorizes candidates into different skill groups using clustering techniques.

This project demonstrates the practical implementation of Machine Learning concepts, Flask backend integration, and modern frontend development.

---

##  Project Objectives

- Automate internship candidate evaluation.
- Reduce manual screening efforts.
- Implement Machine Learning algorithms in a real-world application.
- Demonstrate supervised and unsupervised learning concepts.
- Create a professional and interactive web application.
- Integrate frontend and backend technologies.

---

##  Technologies Used

### Programming Language

- Python

### Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

### Backend

- Flask

### Machine Learning Libraries

- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Development Environment

- Visual Studio Code

---

##  Machine Learning Concepts Implemented

### Supervised Learning

- K-Nearest Neighbors (KNN)
- Logistic Regression
- Decision Tree
- Random Forest

### Unsupervised Learning

- K-Means Clustering

---

##  Dataset Features

The system evaluates candidates based on the following parameters:

- CGPA
- Technical Skills
- Aptitude Score
- Communication Skills
- Projects Completed
- Certifications
- GitHub Score
- LinkedIn Score

---

##  Project Workflow

### Step 1

User enters candidate information.

### Step 2

The Flask backend receives the data.

### Step 3

Machine Learning models analyze the candidate profile.

### Step 4

Random Forest predicts candidate suitability.

### Step 5

K-Means categorizes candidates into skill groups.

### Step 6

Results are displayed through an interactive interface.

---

##  Project Structure

```text
IntelliHire_AI/

│── app.py

│── train_models.py

│── dataset/

│   └── candidate_dataset.csv

│── models/

│   ├── knn.pkl

│   ├── logistic.pkl

│   ├── decision.pkl

│   ├── rf_model.pkl

│   └── kmeans.pkl

│── templates/

│   ├── index.html

│   └── result.html

│── static/

│   └── style.css

│── requirements.txt

└── README.md
```

---

##  Installation Guide

### Clone the repository

```bash
git clone https://github.com/your-username/IntelliHire-AI.git

cd IntelliHire-AI
```

### Install dependencies

```bash
pip install flask pandas scikit-learn joblib numpy
```

### Train Machine Learning models

```bash
python train_models.py
```

### Run the application

```bash
python app.py
```

### Open in browser

```text
http://127.0.0.1:5000
```

---

##  User Interface Features

- Professional modern design
- Responsive layout
- Hover animations
- Interactive forms
- Typing animations
- Floating background effects
- Smooth transitions

---

##  Candidate Categories

The system groups candidates into:

###  Industry Ready

Candidates with excellent performance.

###  Potential Candidate

Candidates with moderate performance.

###  Needs Training

Candidates requiring additional improvement.

---

##  Advantages

- Reduces manual screening effort
- Faster evaluation process
- Interactive user experience
- Industry-oriented implementation
- Practical Machine Learning application
- Easy to understand and maintain

---

##  Future Enhancements

- Resume upload functionality
- PDF report generation
- Candidate ranking system
- Admin dashboard
- Database integration
- Email notifications
- Analytics dashboard

---

##  Learning Outcomes

Through this project, practical knowledge was gained in:

- Machine Learning concepts
- Data preprocessing
- Model training
- Classification algorithms
- Clustering algorithms
- Flask web development
- Frontend and backend integration
- User interface design

---

##  Conclusion

IntelliHire AI demonstrates how Artificial Intelligence and Machine Learning can be integrated into modern recruitment systems. The project successfully combines intelligent decision-making techniques with web technologies to automate internship candidate screening and improve evaluation efficiency.
