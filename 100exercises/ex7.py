<<<<<<< HEAD
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s x %s = %s" % (i,j,i*j))

# end作为参数可以让print打印在同一行，print()可以换下一行

import time
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" % (i,j,i*j),end=" ")
    print()
    time.sleep(1)
=======
# ex7.py

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(30))
>>>>>>> 2a24b5eda7ec3bea0b1ef131d6677e7293a14dec
