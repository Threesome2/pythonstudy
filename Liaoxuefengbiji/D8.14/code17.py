#code17.py

#'12345'-->12345

from functools import reduce

Digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}


def str2int(s):
    
    def str2s(s):
        return Digits[s]    

    def cal(x,y):
        return x*10+y
    num=reduce(cal,map(str2s,s))
    return num

print(str2int('00000'))





