# ex14.py

import math
# from functools import reduce

def ifzhi(num):
    a=math.sqrt(num)
    for i in range(2,int(a+2)):
        if num%i ==0:
            return i,num/i
    return 0,0

# def printff(a=1,b=1):
#     print('%d x %d'%(a,b))

for i in range(1,50):
    L=[]
    a,b=ifzhi(i)
    if a==0:
        print("%d = 1 x %d"%(i,i))
        continue
    while a != 0:
        L.append(a)
        c=b
        a,b=ifzhi(b)
        if a == 0:
            if c!= 1:
                L.append(c)
    print("%d = "%i,end=" ")
    
    # reduce(printff,L)
    j=0
    for k in L:
        print("%d"%k,end=" ")
        if j<len(L)-1:
            j+=1
            print("x",end=" ")
    print()
