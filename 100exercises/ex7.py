# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s x %s = %s" % (i,j,i*j))

# end作为参数可以让print打印在同一行，print()可以换下一行

import time
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" % (i,j,i*j),end=" ")
    print()
    time.sleep(1)