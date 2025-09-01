def fun(a=(),b=[]):
    a += (1,)
    b.append(1)
    return a,b
fun()
print(fun())

