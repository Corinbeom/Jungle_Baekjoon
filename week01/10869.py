def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def remain(a,b):
    return a % b


a, b = map(int, input().split())


res = plus(a,b)
print(res)
res = minus(a,b)
print(res)
res = multiply(a,b)
print(res)
res = divide(a,b)
print("%d" %res)
res = remain(a,b)
print(res)