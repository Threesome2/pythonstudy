#list和tuple
classmates = ['Michale','Bob','Tom','Jim']
#print(classmates)

def index():
    print(len(classmates))
    #print(classmates[0])
    for i in range(0,len(classmates)):
        print(classmates[i])    

    # for name in classmates:
    #     print(name)
    print(classmates[-1])

def insertmenber():
    print(classmates)
    #在末尾追加元素
    classmates.append('Adam')
    print("在末尾追加元素:%s"%classmates[-1])
    #在第三个元素后面插入元素Tom2
    classmates.insert(2,'Tom2')
    print("在第2个索引位置插入元素Tom2")
    print(classmates)

def Pop():
    print(classmates)
    classmates.pop()
    print('删除末尾元素')
    print(classmates)
    a=classmates.pop(-1)
    print(a)
    print(classmates)


# insertmenber()
# Pop()


list1 =['A','B']
tuple1 = (0,1,2,list1)
list1.pop()

# tuple1[3][0]='X'
# tuple1[3][1]='Y'
print(tuple1)

