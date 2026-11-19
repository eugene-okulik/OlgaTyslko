def repeat_me(func):
    def wrapper(*args, count=1):
        result = None
        for i in range(count):
            result = func(*args)
        return result

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


def repeat_me_2(count=1):
    def decorator(func):
        def wrapper(*args):
            result = None
            for _ in range(count):
                result = func(*args)
            return result

        return wrapper

    return decorator


@repeat_me_2(count=2)
def example_2(text):
    print(text)


example_2('print me')
