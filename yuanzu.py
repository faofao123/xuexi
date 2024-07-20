#元组是不可变序列
#元组名=(element1,element2,……,elementN)
#元组名=tuple(序列)
#删除：del 元组名
t=('hello',[1,2,3],'world')
print(t)
t=tuple('helloworld')
print(t)
t=tuple([1,2,3,4])
print(t)

print(1 in t)
print(max(t))
print(min(t))
print(len(t))
print(t.index(2))
print(t.count(2))

#元组只有一个元素，都好也不能省
t_=[10,]
print(t_,type(t_))

del t_