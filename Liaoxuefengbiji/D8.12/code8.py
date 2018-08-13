#code8.py
L = ['Bart', 'Lisa', 'Adam']
i=0
while i<len(L):
    print(L[i])
    i+=1

n=1
while n<=100:
    if n<=10:
        print(n)
    else:
        break
    n+=1
print('END')


def getjishu():
    n=1
    num_ji=[]
    num_ou=[]
    while n<=100:
        if n%2!=0:
            num_ji.append(n)
            # print(num_ji)
        else:
            num_ou.append(n)
        n+=1
    return num_ji,num_ou

numji,numou=getjishu()
print(numji)
print(numou)
print(len(numji))
print(len(numou))


