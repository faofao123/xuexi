#for的语句结构
# for 循环变量 in 遍历对象:
#     语句块

#1 遍历字符串
for i in 'hello':
    print(i)

#2 range()函数，python内置函数，产生一个[n,m)的整数序列，包含n，不包含m
for i in range(1, 11):
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i, '是偶数')

sum = 0#3 求和
for i in range(1, 11):
    sum += i
print(sum)

#for……else……结构
# for 循环变量 in 遍历对象:
#     语句块1
# else:
#     语句块2
for i in range(1, 11):
    sum += i
else:
    print(sum)
#for循环正常结束循环，无非正常中断现象（break）,则执行else语句