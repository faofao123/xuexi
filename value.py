#变量名=value
number = input('请输入：')
print(number, type(number))  #type()函数可以查询变量的数据类型

a = 0.1
b = 0.2
print(a + b)  #不确定的尾数问题
print(round(1 / 3, 1))  #round（）函数精确到n位小数

info = '''
冯元正
221900402
'''
print(info)  #多行字符串

print(number[0:2])  #字符串[a:b]截取下标a到下标b-1的字符串部分，默认从0开始
print(number[:2])  #a默认从0开始
print(number[2:])  #b默认为结尾

print('fyz' in number)  #判断是否为子串

print(bool(number))  #判断是否为空
