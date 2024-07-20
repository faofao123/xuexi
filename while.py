#while语句结构
# while 表达式:
#     语句块
s = 0
i = 1
while i <= 100:
    s = s + i
    i = i + 1
print(s)

# while……else……结构
# while 循环变量:
#     语句块1
# else:
#     语句块2
s = 0
i = 1
while i <= 100:
    s = s + i
    i = i + 1
else:
    print(s)
#循环正常结束，执行else语句