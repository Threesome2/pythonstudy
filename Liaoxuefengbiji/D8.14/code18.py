#code18.py
#['adam', 'LISA', 'barT']-->['Adam', 'Lisa', 'Bart']


def str_cap(name):
    name_norm=''
    for s in name:
        name_norm+=s.lower()
    name_norm=name_norm[0].upper()+name_norm[1:len(name_norm)]
    return name_norm


# L=['adam', 'LISA', 'barT']
# L1=list(map(str_cap,L))
# print(L1)


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(str_cap, L1))
print(L2)




