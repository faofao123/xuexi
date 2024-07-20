#列表生成式
#list=[expression for item in range]
#list=[expression for item in range if condition]
import random
list1=[item for item in range(1,11)]
print(list1)
list2=[item*item for item in range(1,11)]
print(list2)
list3=[random.randint(1,100) for item in range(1,11)]
print(list3)

list4=[i for i in range(10) if i%2==0]
print(list4)

#二维列表
lst1=[
    [1,2,3]
    ,[4,5,6]
    ,[7,8,9]
]
print(lst1)

for row in lst1:
    for item in row:
        print(item,end=' ')
    print()

lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)