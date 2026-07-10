# import streamlit as st
# import pandas as pd

# from recommendation import recommend_courses

# profile = pd.read_csv("Student_Clusters.csv")

import streamlit as st
import pandas as pd
from recommendation import recommend_courses

# Load student data
profile = pd.read_csv("Student_Clusters.csv")

# Title
st.title("🎓 EduPro Course Recommendation System")

# Student selection
user = st.selectbox("Select Student", profile["UserID"].unique())

# Button
if st.button("Recommend Courses"):

    rec = recommend_courses(user)

    if rec.empty:
        st.warning("No recommendations found.")
    else:
        st.success("Recommended Courses")
        st.dataframe(
            rec[
                [
                    "CourseID",
                    "CourseCategory",
                    "CourseLevel",
                    "CourseRating"
                ]
            ]
        )