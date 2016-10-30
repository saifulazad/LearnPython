from functools import wraps


def debug(prefix = ''):

    def decorate(func):
        msg = func.__qualname__

        @wraps(func)
        def wrapper(*args, **kwargs):

            print(prefix + msg)
            return func(*args, **kwargs)

        return wrapper

    return decorate

@debug(prefix='***')
def add(x, y):
    return x+y



add(1,5)
