def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        c = b
        b = a + b
        a = c
    return b

def fac(n):
    a = 1
    for x in range(1, n+1):
        a = a * x
    return a

print(fac(4))
