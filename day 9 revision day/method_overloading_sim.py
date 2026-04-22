class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(2))
print(m.add(2,3))
print(m.add(2,3,4))