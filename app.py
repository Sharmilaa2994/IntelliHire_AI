from flask import Flask,render_template,request
import joblib

app=Flask(__name__)

rf=joblib.load("models/rf_model.pkl")

kmeans=joblib.load("models/kmeans.pkl")

@app.route('/')

def home():

    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():

    cgpa=float(request.form['cgpa'])

    tech=int(request.form['tech'])

    aptitude=int(request.form['aptitude'])

    communication=int(request.form['communication'])

    projects=int(request.form['projects'])

    certifications=int(request.form['certifications'])

    github=int(request.form['github'])

    linkedin=int(request.form['linkedin'])

    values=[[
    cgpa,
    tech,
    aptitude,
    communication,
    projects,
    certifications,
    github,
    linkedin
    ]]

    prediction=rf.predict(values)

    cluster=kmeans.predict(values)

    if prediction[0]==1:

        result="Highly Suitable"

    else:

        result="Needs Improvement"

    cluster_names={

    0:"Industry Ready",

    1:"Potential Candidate",

    2:"Needs Training"

    }

    return render_template(

    "result.html",

    prediction=result,

    cluster=cluster_names[cluster[0]]

    )

if __name__=="__main__":

    app.run(debug=True)