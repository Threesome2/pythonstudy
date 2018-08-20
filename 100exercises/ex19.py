# ex19.py
# refer to ex14.py

for k in range(1,1001):
    L=[]
    e=0
    for i in range(1,k):
        if k%i==0:
            L.append(i)
            e+=i
            # print(i)
            # print('e:',e)
    if k == e:
        print(k)
        for k in L:
            print(k, end=' ')
        print()
    # print('---',k)
    # for k in L:
    #     print(k,end= " ")
    # print()