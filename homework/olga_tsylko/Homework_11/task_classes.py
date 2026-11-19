class Book:
    material = 'бумага'
    isText = True

    def __init__(self, title, author, page_counter, ISBN, isReserved=False):
        self.title = title
        self.author = author
        self.page_counter = page_counter
        self.ISBN = ISBN
        self.isReserved = isReserved

    def get_info(self):
        info = (
            f"Название: {self.title}, Автор: {self.author}, "
            f"страниц: {self.page_counter}, материал: {self.material}"
        )
        if self.isReserved:
            info += ", зарезервирована"
        return info


class SchoolBooks(Book):
    def __init__(self, title, author, page_counter, ISBN, school_subject, classroom, is_tasks, isReserved=False):
        super().__init__(title, author, page_counter, ISBN, isReserved)
        self.school_subject = school_subject
        self.classroom = classroom
        self.is_tasks = is_tasks
        self.isReserved = isReserved

    def get_info(self):
        info = (
            f"Название: {self.title}, Автор: {self.author}, "
            f"страниц: {self.page_counter}, предмет: {self.school_subject}, класс: {self.classroom}"
        )
        if self.isReserved:
            info += ", зарезервирована"
        return info


book_1 = Book("Идиот", "Достоевский", 500, True)
book_2 = Book("Война и мир", "Толстой", 1000, True)
book_3 = Book("Игрок", "Достоевский", 100, True)
book_4 = Book("Евгений Онегин", "Пушкин", 200, True)
book_5 = Book("Золотая рыбка", "Пушкин", 70, True)
book_5.isReserved = True
print(book_1.get_info())
print(book_2.get_info())
print(book_3.get_info())
print(book_4.get_info())
print(book_5.get_info())

school_book1 = SchoolBooks(
    "История Древнего мира", "Кушнир", 300,
    False, "Всемирная история", 5, True
)
school_book2 = SchoolBooks(
    "Алгебра", "Иванова", 300,
    False, "Математика", 5, True
)
school_book3 = SchoolBooks(
    "Литература", "Малышева", 90,
    False, "Русская литература", 5, False
)
school_book2.isReserved = True
print(school_book1.get_info())
print(school_book2.get_info())
print(school_book3.get_info())
