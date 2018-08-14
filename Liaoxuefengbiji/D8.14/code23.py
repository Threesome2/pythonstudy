#code23.py


# -*- coding: utf-8 -*-

L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    x,y =t
    return x

def by_score(t):
    x,y =t
    return y

L2=sorted(L1, key=by_name,reverse=True)
print(L2)





