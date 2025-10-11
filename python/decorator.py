from functools import wraps
def func(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("hello world")
        result = f(*args, **kwargs)
        return result