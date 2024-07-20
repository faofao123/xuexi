#模拟用户登录
# i=0
# while i<3:
#     user=input('请输入用户名：')
#     password=input('请输入密码：')
#     if user=='fyz' and password=='200407':
#         print('请稍后，系统正在登录中……')
#         i=4
#     else:
#         if i<2:
#             print('你还有',2-i,'次机会')
#         i=i+1
# if i==3:
#     print('错误')

#循环打印
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print('*',end='')
    print()

#三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(end=' ')
    for k in range(1,2*i):
        print('*',end='')
    print()

