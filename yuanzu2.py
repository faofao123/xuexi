#遍历元组
t=('python','hello','world')
print(t[0])
t1=t[0:3:2]
print(t1)

for i in t:
    print(i,end=' ')
print()

for i in range(len(t)):
    print(t[i],end=' ')
print()

for i,item in enumerate(t):
    print(i,item)
print()
for i,item in enumerate(t,start=1):
    print(i,item)
print()

#元组生成式
t=(i for i in range(10))
print(t)
t=tuple(t)
print(t)