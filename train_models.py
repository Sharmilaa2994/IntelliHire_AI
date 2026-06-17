import pandas as pd
import joblib

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans

data=pd.read_csv("dataset/candidate_dataset.csv")

X=data.drop("Suitability",axis=1)

y=data["Suitability"]

knn=KNeighborsClassifier()

knn.fit(X,y)

joblib.dump(knn,"models/knn.pkl")

logistic=LogisticRegression()

logistic.fit(X,y)

joblib.dump(logistic,"models/logistic.pkl")

decision=DecisionTreeClassifier()

decision.fit(X,y)

joblib.dump(decision,"models/decision.pkl")

forest=RandomForestClassifier()

forest.fit(X,y)

joblib.dump(forest,"models/rf_model.pkl")

kmeans=KMeans(
n_clusters=3,
random_state=42
)

kmeans.fit(X)

joblib.dump(kmeans,"models/kmeans.pkl")

print("Models Created Successfully")