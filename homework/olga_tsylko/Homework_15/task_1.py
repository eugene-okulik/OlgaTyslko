import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port='25060',
    database='st-onl'
)

cursor = db.cursor(dictionary=True)


def insert_and_get(cursor, db, table_name, columns, values):
    columns_str = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(columns))
    query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({placeholders})"
    cursor.execute(query, values)
    db.commit()

    new_id = cursor.lastrowid
    cursor.execute(f"SELECT * FROM `{table_name}` WHERE id = %s", (new_id,))
    record = cursor.fetchone()
    print(f"Добавлено в {table_name}:", record)
    return record


def select_and_show(cursor, query, params=None):
    cursor.execute(query, params or ())
    records = cursor.fetchall()
    for row in records:
        print(row)
    return records


student = insert_and_get(
    cursor, db,
    "students",
    ["name", "second_name", "group_id"],
    ("Alex", "Novik", None)
)
student_id = student["id"]

book_1 = insert_and_get(
    cursor, db, "books", ["title", "taken_by_student_id"], ('ИИ для всех', student_id)
)
book_2 = insert_and_get(
    cursor, db, "books", ["title", "taken_by_student_id"], ('Cybersafety 3', student_id)
)
new_group = insert_and_get(
    cursor, db,
    "groups",
    ["title", "start_date", "end_date"],
    ('Python course', 'nov 2026', 'dec 2026')
)
my_group_id = new_group["id"]

update_query = "UPDATE students SET group_id=%s WHERE id=%s"
cursor.execute(update_query, (my_group_id, student_id))
db.commit()
select_and_show(cursor, "SELECT * FROM students WHERE id = %s", (student_id,))

subject_1 = insert_and_get(
    cursor, db, "subjects", ["title"], ('Кибербезопасность: основы',)
)
subject_1_id = subject_1["id"]

subject_2 = insert_and_get(
    cursor, db, "subjects", ["title"], ('Статистика',)
)
subject_2_id = subject_2["id"]

lesson_1 = insert_and_get(
    cursor, db, "lessons", ["title", "subject_id"], ('Статистика: введение', subject_2_id)
)
lesson_1_id = lesson_1["id"]

lesson_2 = insert_and_get(
    cursor, db, "lessons", ["title", "subject_id"],
    ('Анализ данных', subject_2_id)
)
lesson_2_id = lesson_2["id"]

lesson_3 = insert_and_get(
    cursor, db, "lessons", ["title", "subject_id"],
    ('Введение в Кибербезопасность', subject_1_id)
)
lesson_3_id = lesson_3["id"]

lesson_4 = insert_and_get(
    cursor, db, "lessons", ["title", "subject_id"], ('Введение в антивирусы', subject_1_id)
)
lesson_4_id = lesson_4["id"]

mark_1 = insert_and_get(
    cursor, db, "marks", ["value", "lesson_id", "student_id"], (9, lesson_1_id, student_id)
)
mark_2 = insert_and_get(
    cursor, db, "marks", ["value", "lesson_id", "student_id"], (7, lesson_2_id, student_id)
)
mark_3 = insert_and_get(
    cursor, db, "marks", ["value", "lesson_id", "student_id"], (8, lesson_3_id, student_id)
)
mark_4 = insert_and_get(
    cursor, db, "marks", ["value", "lesson_id", "student_id"], (10, lesson_4_id, student_id)
)

marks = select_and_show(
    cursor,
    "SELECT `value` AS marks FROM marks WHERE student_id = %s",
    (student_id,)
)
books = select_and_show(
    cursor,
    "SELECT title FROM books WHERE taken_by_student_id = %s",
    (student_id,)
)
full_info = select_and_show(
    cursor,
    """
    SELECT
        st.id AS student_id,
        st.name,
        st.second_name,
        g.title AS group_title,
        b.title AS book_title,
        m.value AS mark,
        l.title AS lesson_title,
        s.title AS subject_title
    FROM students st
    LEFT JOIN `groups` g ON g.id = st.group_id
    LEFT JOIN books b ON st.id = b.taken_by_student_id
    LEFT JOIN marks m ON st.id = m.student_id
    LEFT JOIN lessons l ON l.id = m.lesson_id
    LEFT JOIN subjects s ON s.id = l.subject_id
    WHERE st.id = %s
    """,
    (student_id,)
)
db.close()
