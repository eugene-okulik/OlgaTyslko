a, b = map(int, input("Type 2 digits ").split())


def dec_funct(func):
    def wrapper(x, y, operation=None):
        if x < 0 or y < 0:
            operation = '*'
        elif x == y:
            operation = '+'
        elif x > y:
            operation = '-'
        else:
            operation = '/'
        return func(x, y, operation)

    return wrapper


@dec_funct
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return 'Try again'


print(calc(a, b))
