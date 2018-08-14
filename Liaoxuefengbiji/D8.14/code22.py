#code22.py
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    S=[]
    W=[]
    for s in t:
        S.append(s[0])
    print(S)
    S=sorted(S)
    print(S)
    for s in S:
        for i in t:
            if i[0]==s:
                W.append(i)
    return W

a=by_name(L)
print(a)



