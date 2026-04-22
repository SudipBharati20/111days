class A:
    def funcA(self):
        print("A")

class B(A):
    def funcB(self):
        print("B")

class C(B):
    def funcC(self):
        print("C")

c = C()
c.funcA()
c.funcB()
c.funcC()