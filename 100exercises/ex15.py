# ex15.py
import string
import time
# help(string)
# a=input('请输入一串字符：\n')

L={'英文字母':0,'空格':0,'数字':0,'其他字符':0}
print(L['空格'])
a='as  d1asd ass~`1d1'
for k in a:
    if k.isalpha():
        L['英文字母']+=1
    elif k==' ':
        L['空格']+=1
    elif k.isdigit():
        L['数字']+=1
        # print('111111')
    else:
        L['其他字符']+=1

for k in L:
    print(k, L[k])
    time.sleep(1)


