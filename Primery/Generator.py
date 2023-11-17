for i in range(5):
    print(i)

a = [i for i in range(5)]       # [0, 1, 2, 3, 4]
print(a)
print(type(a))

b = (i for i in range(5))
print(b)
print(type(b))

print(next(b))
print(next(b))