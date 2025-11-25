# dashboard.py
import streamlit as st
import pandas as pd
import os

# -----------------------------
# Load CSVs
# -----------------------------
project_dir = os.path.dirname(os.path.abspath(__file__))

students = pd.read_csv(os.path.join(project_dir, "data", "students.csv"))
courses = pd.read_csv(os.path.join(project_dir, "data", "courses.csv"))
enrollments = pd.read_csv(os.path.join(project_dir, "data", "enrollments.csv"))

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="UC Smart Manufacturing Analytics", layout="wide")

st.title("UC Smart Manufacturing Analytics Dashboard")

# KPIs
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(students))
col2.metric("Total Courses", len(courses))
col3.metric("Total Enrollments", len(enrollments))

# Students by Major
st.subheader("Students by Major")
students_major = students.groupby('major').size().reset_index(name='count')
st.bar_chart(data=students_major, x='major', y='count')

# Courses overview
st.subheader("Courses Offered")
st.dataframe(courses)

# Enrollments overview
st.subheader("Enrollments")
st.dataframe(enrollments)

# Optional: Future extension placeholder
st.info("Future extension: Add interactive visualizations or dashboards with Plotly/Streamlit components here.")
