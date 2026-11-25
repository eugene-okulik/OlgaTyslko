INSERT INTO students (name, second_name, group_id) VALUES ('Vladislav', 'Ivanov', NULL)
INSERT INTO books (title, taken_by_student_id) VALUES ('ИИ для чайников', 100003)
INSERT INTO books (title, taken_by_student_id) VALUES ('Кибербезопасность', 100003)
INSERT INTO `groups`(title, start_date, end_date) VALUES ('Программирование на Python', 'nov 2026', 'dec 2026')
UPDATE students SET group_id = 25217 WHERE id = 100003
INSERT INTO subjects (title) VALUES ('Кибербезопасность')
INSERT INTO subjects (title) VALUES ('Статистика')
INSERT INTO lessons (title, subject_id) VALUES ('Общая теория статистики', 23925)
INSERT INTO lessons (title, subject_id) VALUES ('Демографическая статистики', 23925)
INSERT INTO lessons (title, subject_id) VALUES ('Антивирусы', 23926)
INSERT INTO lessons (title, subject_id) VALUES ('SQL иньекции', 23926)
INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 77613, 100003)
INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 77614, 100003)
INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 77615, 100003)
INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 77616, 100003)

SELECT `value` as marks  FROM marks where student_id = 100003
SELECT title FROM books where taken_by_student_id = 100003
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
LEFT JOIN `groups`g ON g.id = st.group_id
LEFT JOIN books b ON st.id = b.taken_by_student_id
LEFT JOIN marks m ON st.id = m.student_id
LEFT JOIN lessons l ON l.id = m.lesson_id
LEFT JOIN subjects s ON s.id = l.subject_id
WHERE st.id = 100003
