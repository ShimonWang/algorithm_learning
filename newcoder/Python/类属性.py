class Base(object):

    count = 0

    def __init__(self):

        pass
b1 = Base()
b2 = Base()

b1.count = b1.count + 1

print(b1.count,end=" ")

print(Base.count,end=" ")

print(b2.count)

牛客 = 3
print(牛客)