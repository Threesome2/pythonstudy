#code15.py

d={'x':'A','y':'B','z':'C'}

for key,value in d.items():
    print(key,'=',value)


c=[k+'='+v for k,v in d.items()]
print(c)


L=['A','B','C','D']
e=[s.lower() for s in L ]
print(e)


