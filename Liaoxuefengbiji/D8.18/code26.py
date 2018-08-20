# !/user/bin/env python3
#可以让hellp.py直接在unix上运行
# -*- coding:utf-8 -*-
#上面两行是标注注释

'a test module'   #第一个字符串表示模块的文档注释

__auther__='Jack Son'

print(__auther__)

import sys

def test():
    args = sys.argv # 这个argv变量用list存储了命令行所有的参数,第一个元素是文件名

    if len(args)==1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello,%s'%args[1])
    else:
        print('Too many arguments!')


# for k in sys.argv:
#     print(k)
print(sys.argv[0])

print(__doc__)

if __name__=='__main__':
    test()







