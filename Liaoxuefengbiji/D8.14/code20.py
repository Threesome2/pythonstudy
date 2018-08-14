#code20.py
#str2float:'123.456'-->123.456
from functools import reduce

Digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2float(s):
    #找到‘.’
    for i in range(20):
        if s[i]=='.':
            break
    
    index = len(s)-i-1
    
    s=s[:i]+s[i+1:]
    
    def str2s(s):
        return Digits[s]  
    
    def cal1(x,y):
        return x*10+y

    s=reduce(cal1,map(str2s,s))/(10**index)
    return s

a=str2float('0121231233.45234236')
print(a)


