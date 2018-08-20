# ex13.py
import time
t1=time.time()
for k in range(100,100000):
    # print(k)
    a=k//100
    # print(a)
    b=(k-a*100)//10
    # print(b)
    c=(k-a*100-b*10)
    if a**3+b**3+c**3==k:
        print(k,end=" ")
t2=time.time()
print('执行时间：%f'%(t2-t1))

t1=time.time()
for i in range(100, 100000):
    s = str(i)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == i:
        print(i)
t2=time.time()
print('执行时间：%f'%(t2-t1))
