CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    major VARCHAR(50)
);
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    credits INT
);
CREATE TABLE enrollments (
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    enrollment_date DATE,
    grade CHAR(1),
    PRIMARY KEY (student_id, course_id)
);