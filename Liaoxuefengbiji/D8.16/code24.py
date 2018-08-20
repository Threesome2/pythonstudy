# code24.py 
#不带参数的decorator
import time
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper



@log
def now():
    # print(time.localtime(time.time()))
    t=time.strftime('%Y.%m.%d',time.localtime(time.time()))
    print(t)

print("第一次调用：")
now()
print(now.__name__)





