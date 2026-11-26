import mysql.connector as mysql
import dotenv
import os
import csv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

base_path = os.path.dirname(os.path.abspath(__file__))
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

query = """
    SELECT
        st.name as name,
        st.second_name,
        g.title AS group_title,
        b.title AS book_title,
        s.title AS subject_title,
        l.title AS lesson_title,
        m.value AS mark_value
    FROM students st
    INNER JOIN `groups` g ON g.id = st.group_id
    INNER JOIN books b ON st.id = b.taken_by_student_id
    INNER JOIN marks m ON st.id = m.student_id
    INNER JOIN lessons l ON l.id = m.lesson_id
    INNER JOIN subjects s ON s.id = l.subject_id
    WHERE st.name = %s 
    AND st.second_name = %s 
    AND g.title = %s 
    AND b.title = %s
    AND s.title = %s
    AND l.title = %s
    AND m.value = %s
    """

with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
    csv_data = list(csv.DictReader(csv_file))

cursor = db.cursor(dictionary=True)

for row in csv_data:
    values = (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        row['mark_value'],
    )
    cursor.execute(query, values)
    if not cursor.fetchall():
        print(row)

db.close()
