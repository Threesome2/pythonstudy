import time

def sumOfN(n):
    start=time.time()
    sum1=1
    for i in range(1,n+1):
        sum1+=i
        # print(sum1)
    end=time.time()
    return sum1, end-start


sum1,t=sumOfN(300)
print(sum1,t)

for i in range(5):
    print("Sum is %d required %10.7f second"%sumOfN(100000))


