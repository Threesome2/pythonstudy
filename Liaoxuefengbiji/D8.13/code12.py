#code12.py


def trim(strs):
    if strs=='':
        return strs
    i=0
    while strs[i] == ' ':
        if i == len(strs)-1:
            return ''
        i+=1
    j=-1
    while strs[j] == ' ':
        j-=1
    # print(i ,j)
    str_trim=strs[i:len(strs)+j+1]
    print(str_trim)
    return str_trim


# strs=trim('   asda  sd')
# print(strs,'1')

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')