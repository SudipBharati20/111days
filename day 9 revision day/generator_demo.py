def count(n):
    for i in range(n):
        yield i

for num in count(5):
    print(num)