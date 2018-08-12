#code9.py
def Loop_continue(a):
    n=1
    num_ji=[]
    while n<=a:
        if n%2==0:
            n+=1
            continue
        num_ji.append(n)
        n+=1
    return num_ji

num_ji=Loop_continue(30)
print(num_ji)