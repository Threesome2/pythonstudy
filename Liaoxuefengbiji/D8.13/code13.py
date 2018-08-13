#code13.py

def findMinAndMax(L):
    if L==[]:
        return None,None
    Max=L[0]
    Min=L[0]
    for i,value in enumerate(L):
        if value>Max:
            Max=value
        elif value<Min:
            Min=value
    return Min,Max


# L=list(range(10))
# Max,Min=findMinAndMax(L)
# print(Max,Min)


# 测试
if findMinAndMax([]) != (None, None):
    print(1)
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print(2)
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print(3)
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')