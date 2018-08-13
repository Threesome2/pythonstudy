#code14.py


a=[x for x in range(100) if x%2 == 0]
print(len(a))
print(a)


#全排列
a=[m+n for m in 'ABC' for n in 'XYZ']
print(a)


import os

dirs=[d for d in os.listdir('.')]

print(dirs)
