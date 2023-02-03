from functools import wraps

def args_limiter(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        return fn(*args, **kwargs)
    return wrapper

@args_limiter
def return_math(a, b, c):
    suma = sum(a + b + c)
    return suma
print(return_math(2, 4, 5))