import pandas as pd

profile = pd.read_csv("Student_Clusters.csv")
recommendations = pd.read_csv("Recommendations.csv")

def recommend_courses(user_id):
    rec = recommendations[recommendations["UserID"] == user_id]
    return rec