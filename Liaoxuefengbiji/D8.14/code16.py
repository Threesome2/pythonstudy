#code16

L = ['Hello', 'World', 18, 'Apple', None]
 
# L2=[s.lower() for s in L if isinstance(s, str) ]
L2=[]
# for s in L :
#     if isinstance(s,str):
#         L2.append(s.lower())
#     else:
#         L2.append(s)

def f(k):
    if isinstance(k,str):
        return k.lower()
    else:
        return k


# def f(k):
#     return k.lower() or k


L2=list(map(f,L))



# 测试:
print(L2)
if L2 == ['hello', 'world', 18,'apple',None]:
    print('测试通过!')
else:
    print('测试失败!')











