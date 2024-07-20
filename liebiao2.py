#列表的相关操作
#list.append(x)在列表最后增加一个元素
# list.insert(index,x)在列表中第index位置增加一个元素
# list.clear()清除所有元素
# list.pop(index)将列表中第index位置元素取出，并删除
# list.remove(x)将列表中出现的第一个x删除
# list.reverse()将列表中的元素反转
# list.copy()拷贝所有元素，生成一个新的列表
list=['hello','world','python']
list.append('sql')
print(list)

list.insert(0,'100')
print(list)

list.remove('100')
print(list)

print(list.pop(0))
print(list)

list.reverse()
print(list)

newlist=list.copy()
print(newlist)

list.clear()
print(list)