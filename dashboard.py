import streamlit as st
import psycopg2
import pandas as pd
import os

from database import connect_db, load_csv

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="UC Smart Manufacturing Dashboard", layout="wide")

st.title("UC Smart Manufacturing Analytics Dashboard")

# -----------------------------
# Connect to DB
# -----------------------------
conn = connect_db()
if not conn:
    st.error("Cannot connect to database")
    st.stop()

# -----------------------------
# Load CSVs safely (only if empty)
# -----------------------------
project_dir = os.path.dirname(os.path.abspath(__file__))
load_csv(conn, "students", os.path.join(project_dir, "data", "students.csv"))
load_csv(conn, "courses", os.path.join(project_dir, "data", "courses.csv"))
load_csv(conn, "enrollments", os.path.join(project_dir, "data", "enrollments.csv"))

# -----------------------------
# Read data into pandas
# -----------------------------
students_df = pd.read_sql("SELECT * FROM students;", conn)
courses_df = pd.read_sql("SELECT * FROM courses;", conn)
enrollments_df = pd.read_sql("SELECT * FROM enrollments;", conn)

# -----------------------------
# Students overview
# -----------------------------
st.subheader("Students")
st.dataframe(students_df)

# Students count by major
st.subheader("Students by Major")
major_counts = students_df['major'].value_counts()
st.bar_chart(major_counts)

# -----------------------------
# Courses overview
# -----------------------------
st.subheader("Courses")
st.dataframe(courses_df)

# Course counts
st.subheader("Number of Courses by Credits")
credit_counts = courses_df['credits'].value_counts()
st.bar_chart(credit_counts)

# -----------------------------
# Enrollments overview
# -----------------------------
st.subheader("Enrollments")
st.dataframe(enrollments_df)

# Enrollments per course
st.subheader("Enrollments per Course")
enroll_counts = enrollments_df.groupby('course_id').size()
st.bar_chart(enroll_counts)

# -----------------------------
# Future Extension
# -----------------------------
st.info("Future extension: Interactive dashboards with filters, Plotly charts, and KPIs for finance & operations")
