import sys

sys.set_int_max_str_digits(0)


def fibonach():
    a = 0
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c


count = 1
for number in fibonach():
    if count in (5, 200, 1000, 100000):
        print(number)
    if count == 100000:
        break
    count += 1
