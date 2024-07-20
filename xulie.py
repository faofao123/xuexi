#切片操作  序列[start:end:step]  step步长默认为1
#序列索引0~N-1，-N~-1  (之前value.py文件中有详细写)
s=input('请输入字符串：')
s1=s[0:1:1]
s2=s[0:3:2]
print(s1,s2,sep='\n')

#逆序输出
print(s[::-1])

#序列的相加与相乘
x1='hello'
x2='world'
print(x1+x2)
print(x1*2)

#操作函数
# x in s      判断x是否在s中
# x not in s
# len(s)      s的长度
# max(s)      s中元素的最大值
# min(s)      s中元素的最小值
# s.index(x)  s中x出现的第一次位置
# s.count(x)  s中出现x的次数
print('f' in s)
print(len(s))
print(max(s))#ASCII
print(min(s))
print(s.index('y'))
print(s.count('z'))

