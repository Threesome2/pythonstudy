# ex18.py

k=5
n=3
sum = 0
for i in range(1,n+1):
    j = 1
    sum2 = 0 
    for j in range(1,i+1):
        sum2 += k*(10**(j-1))
        
    sum += sum2


print(sum)