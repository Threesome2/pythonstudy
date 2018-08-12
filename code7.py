#code7.py

def forloop(a,b):
    sum1=0
    for i in range(a,b+1):
        sum1 =sum1+ i
        # print(sum1)
    return sum1

        

sum2=forloop(1,10)
print(sum2)
print("sum=%d"%sum2)

def whileloop(a,b):
    i=a
    sum1=0
    print('=====')
    while i<=b:
        sum1+=i
        i+=1
    print(sum1)
    return sum1

sum2=whileloop(2,10)
print(sum2)