SELECT major, COUNT(student_id) AS total_students FROM students GROUP BY major;
SELECT s.major, AVG(
    CASE grade
        WHEN 'A' THEN 4
        WHEN 'B' THEN 3
        WHEN 'C' THEN 2
        WHEN 'D' THEN 1
        ELSE 0
    END
) AS avg_gpa FROM enrollments e JOIN students s ON e.student_id = s.student_id GROUP BY s.major;
SELECT c.course_name, COUNT(e.student_id) AS enrolled_students FROM enrollments e JOIN courses c ON e.course_id = c.course_id GROUP BY c.course_name ORDER BY enrolled_students DESC;