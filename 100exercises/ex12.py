# ex12.py
import math

def ifsu(num):

    b,a=math.modf(math.sqrt(num))

    if b==0:
        print("平方数")
        return False
    else:
        i=1
        for i in range(2,int(a+1)):
            # print("====",num,i)
            if num%i==0:
                return False
        return True

j=0
for i in range(101,201):
    # print(ifsu(i))
    if ifsu(i) ==True:
        j+=1
        print('%d : yes'%i)
    # else:
    #     print('%d : no'%i)
print('总共%d个'%j)