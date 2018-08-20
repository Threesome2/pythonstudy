# ex9.py
import time
print(time.localtime())
f= time.localtime()
# print(str(f.tm_year)+"年"+str(f.tm_mon)+"月"+str(f.tm_mday)+'日'+str(f.tm_hour)+'时')
# for k in f:
#     print(k,end=" ")
# print(type(time.localtime(time.time())))
# print(help(time.strftime))
# print("%s年%s月%s日  %s时%s分%s秒"%(str(time.localtime(time.time()))
i =1
while i<= 60:
    print(time.strftime("%Y-%m-%d  %H:%M:%S",(time.localtime(time.time()))))
    i+=1
    time.sleep(1)