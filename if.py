#if选择结构
num = eval(input('请输入中奖号码：'))
if num % 2 == 0:
    print('中奖')
if num % 2 == 1:
    print('未中奖')

x = input('请输入：')  #判断是否为空字符串
if x:
    print(x + '不是空字符串')
if not x:
    print('空字符串')

#双分支结构
if num % 2 == 0:
    print('中奖')
else:
    print('未中奖')

#多分支结构
score = eval(input('请输入考试分数：'))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')

elif score >= 60:
    print('D')

elif score >= 50:
    print('E')

elif score >= 40:
    print('F')
else:
    print('G')

#and or
user = input('请输入用户名：')
pwd = input('请输入密码：')
if user == 'fyz' and pwd == '123':
    print('密码正确')
else:
    print('密码错误')

#match-case模式匹配
