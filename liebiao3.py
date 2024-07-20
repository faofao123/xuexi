#列表的排序
#list.sort(key=None,reverse=False)   key:排序规则  reverse：升序false，降序true
#sorted(iterable,key=None,reverse=False)   iterable：排序对象
list1=[4,56,3,78,40,56,89]
print(list1)

list1.sort()#排序是在原列表上操作的，不会产生新的列表
print(list1)

list1.sort(reverse=True)#降序
print(list1)

list2=['banana','apple','cat','Orange']
print(list2)

list2.sort()#先排大写，再排小写
print(list2)

list2.sort(key=str.lower) #修改排序规则，都按小写排序
print(list2)

newlist1=sorted(list1)#sorted()函数产生新的列表，不会对原来的列表产生影响
print(newlist1)
print(list1)

newlist2=sorted(list2,key=str.lower, reverse=True)
print(newlist2)
print(list2)