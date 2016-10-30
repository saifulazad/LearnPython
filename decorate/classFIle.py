from functools import wraps


def debug(func):

    msg = func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    for name, val in vars(cls).items():
        if callable(val):

            setattr(cls, name, debug(val))

    return cls


@debugmethods
class Calculator(object):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


ob = Calculator()

