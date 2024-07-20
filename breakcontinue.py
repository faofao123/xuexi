#触发break后，不再执行else部分
i=0
while i<3:
    user=input('请输入用户名：')
    password=input('请输入密码：')
    if user=='fyz' and password=='200407':
        print('请稍后，系统正在登录中……')
        break
    else:
        if i<2:
            print('你还有',2-i,'次机会')
        i=i+1
else:
    print('错误')

#continue跳过本次循环的剩余代码
s=0
for i in range(1,100):
    if i%2==0:
        continue
    s+=i
print(s)#基数和