def singleton(cls):
    cls.__instance = object.__new__(cls)
    cls.__new__ = lambda c, val: cls.__instance
    return cls


@singleton
class A:
    def __init__(self, a):
        self.a = a


a = A(1)
print(a.a)
b = A(3)
print(b.a)
c = A(5)
print(c.a)
print(b.a)
print(a.a)
print(A.__instance)

