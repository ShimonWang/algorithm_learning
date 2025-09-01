def dec(f):
    n = 3

    def wrapper(*args, **kw):
        return f(*args, **kw) * n

    return wrapper


@dec
def foo(n):
    return n * 2

result = foo(2)
print(result)