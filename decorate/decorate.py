
from functools import wraps

def debug(func):

    msg = func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)

    return wrapper


@debug
def add(x,y):
    return x+y

def sub(x,y):
    return x - y;


add(1,1)
e = debug(sub)

print(e(2,2))