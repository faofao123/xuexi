#变量=eval(字符串)去掉字符串最外侧的引号 ，并执行去掉引号后的字符串.常与input（）共同使用
x = eval('10')
print(x, type(x))  #从字符串类型转换成整数类型

y = eval(input('请输入:'))
print(y, type(y))  #从字符串类型转换成浮点类型

hello = 3
print(eval('hello'))  #去掉引号后成为变量
