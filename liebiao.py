#列表是可变序列
#1.列表名=[element1，element2，element3……]
#2.列表名=list(序列)
#删除操作   del列表名
list1=['hello',1,'world']
list2=list('helloworld')
list3=list(range(1,11))
print(list1)
print(list2)
print(list3)
#序列的函数操作都可以使用
print(list1+list2)
print(list2*2)#=list2+list2
print(len(list3))
print(min(list3))
print(list2.index('o'))
print(list2.count('o'))
#删除操作
list4=[1,2,3]
del list4[0]
print(list4)
#列表遍历操作
#enumerate函数
#for index,item in enumerate(list):
#输出index和item(index默认从0开始）
for item in list2:
    print(item,end=' ')
print()

for i in range(0,len(list2)):
    print(list2[i],end=' ')
print()

for i,item in enumerate(list2):
    print(i,item)
print()
for i,item in enumerate(list2,start=1):
    print(i,item)
print()