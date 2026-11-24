import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute('SELECT `value` as marks  FROM marks where student_id = 100003')
marks = cursor.fetchall()
print(marks)
cursor.execute('SELECT title FROM books where taken_by_student_id = 100003')
books = cursor.fetchall()
print(books)
cursor.execute(
    '''SELECT
    st.id AS student_id,
    st.name,
    st.second_name,
    g.title AS group_title,
    b.title AS book_title,
    m.value AS mark,
    l.title AS lesson_title,
    s.title AS subject_title
    FROM students st
    LEFT JOIN `groups`g ON g.id = st.group_id
    LEFT JOIN books b ON st.id = b.taken_by_student_id
    LEFT JOIN marks m ON st.id = m.student_id
    LEFT JOIN lessons l ON l.id = m.lesson_id
    LEFT JOIN subjects s ON s.id = l.subject_id
    WHERE st.id = 100003'''
)
all_data = cursor.fetchall()
print(all_data)
# students = cursor.fetchall()
# for student in students:
#     print(f'<U>: {student[0]}')

# db.close()
