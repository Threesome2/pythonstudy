#code11.py
import math


def quadratic(para):
    a=para[0]
    b=para[1]
    c=para[2]
    deta = b**2-4*a*c
    if deta < 0:
        print("%.fx2+%.fx+%.f 无解"%(a,b,c))
        x1='no'
        x2=0
    elif deta == 0: 
        x1 = (-b)/(2*a)
        x2 = x1
    else:
        x1=(-b+math.sqrt(deta))/(2*a)
        x2=(-b-math.sqrt(deta))/(2*a)
    return x1,x2




para=[6,20,7]

x1,x2=quadratic(para)                    
if x1=='no':
    print('请输入正确的数值')
else:
    print("%.fx2+%.fx+%.f 的解为：\n"%(para[0],para[1],para[2]))
    print("%.1f,%.1f"%(x1,x2))


