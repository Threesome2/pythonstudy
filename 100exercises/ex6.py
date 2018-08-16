# ex6.py

def fib(n):
    a=b=1
    # print(a,b)
    for i in range(n-1):
        a,b=b,a+b
        print(a,b)
    return a

print(fib(30))