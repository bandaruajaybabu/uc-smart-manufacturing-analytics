import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# PAGE SETUP
# ----------------------------------
st.set_page_config(
    page_title="Smart Manufacturing Dashboard",
    layout="wide",
    page_icon="📊",
)

st.title("📊 Smart Manufacturing Analytics Dashboard")
st.write("Interactive academic analytics dashboard built using Streamlit & Plotly.")

# ----------------------------------
# LOAD DATA
# ----------------------------------
students = pd.read_csv("data/students.csv")
courses = pd.read_csv("data/courses.csv")
enrollments = pd.read_csv("data/enrollments.csv")

# Ensure types align
enrollments["course_id"] = enrollments["course_id"].astype(int)
students["student_id"] = students["student_id"].astype(int)

# ----------------------------------
# SUMMARY KPI CARDS
# ----------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎓 Total Students", students.shape[0])

with col2:
    st.metric("📚 Total Courses", courses.shape[0])

with col3:
    st.metric("📝 Total Enrollments", enrollments.shape[0])

# ----------------------------------
# COURSE ENROLLMENT OVERVIEW
# ----------------------------------
st.subheader("📘 Course Enrollment Overview")

enrollments_by_course = (
    enrollments.merge(courses, on="course_id")
    .groupby("course_name")
    .size()
    .reset_index(name="count")
)

if not enrollments_by_course.empty:
    fig_course = px.bar(
        enrollments_by_course,
        x="course_name",
        y="count",
        title="Enrollments per Course",
        text="count",
        color="course_name",
    )
    fig_course.update_traces(textposition="outside")
    fig_course.update_layout(showlegend=False)
    st.plotly_chart(fig_course, width="stretch")
else:
    st.warning("No enrollment data available.")

# ----------------------------------
# STUDENT PROGRESS VIEWER
# ----------------------------------
st.subheader("🎓 Student Progress Viewer")

student_select = st.selectbox(
    "Select a Student",
    students["student_name"].tolist(),
)

selected_id = students.loc[
    students["student_name"] == student_select, "student_id"
].values[0]

student_records = enrollments[enrollments["student_id"] == selected_id]

student_records = student_records.merge(courses, on="course_id", how="left")

st.write(f"### 📄 Records for: {student_select}")

if not student_records.empty:
    st.dataframe(
        student_records[
            ["course_id", "course_name", "enrollment_date", "grade", "credits"]
        ],
        width="stretch",
        hide_index=True,
    )
else:
    st.info("No records available for this student.")

# ----------------------------------
# GRADE DISTRIBUTION
# ----------------------------------
st.subheader("📊 Grade Distribution")

if not enrollments.empty:
    fig_grades = px.histogram(
        enrollments,
        x="grade",
        title="Grade Distribution",
        color="grade",
    )
    fig_grades.update_layout(showlegend=False)
    st.plotly_chart(fig_grades, width="stretch")
else:
    st.warning("No grade data available.")
