#code19.py
from functools import reduce

def prod(L):
    def multy(x,y):
        print(x*y)
        return x*y
    a=reduce(multy,L)
    return a

L=list(range(1,5))
print(prod(L))

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

