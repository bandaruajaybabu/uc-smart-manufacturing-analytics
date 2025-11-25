import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://username:password@localhost:5432/uc_analytics')

students = pd.read_csv('../data/students.csv')
courses = pd.read_csv('../data/courses.csv')
enrollments = pd.read_csv('../data/enrollments.csv')

enrollments['grade'] = enrollments['grade'].str.upper()

students.to_sql('students', engine, if_exists='replace', index=False)
courses.to_sql('courses', engine, if_exists='replace', index=False)
enrollments.to_sql('enrollments', engine, if_exists='replace', index=False)

print("ETL pipeline completed successfully!")