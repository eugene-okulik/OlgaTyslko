def increase_by_10(*args):
    for item in args:
        value = item.split(":")[-1]
        print("Результат сложения:", int(value) + 10)


increase_by_10(
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2",
)
