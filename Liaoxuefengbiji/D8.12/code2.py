print(b'ABC')
x='ABC'.encode('ascii')
print(x)
x='中文'.encode('utf-8')
print(x)
#中文不可用ascii
x=b'ABC'.decode('ascii')
print(x)