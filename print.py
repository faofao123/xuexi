# print(value,……,sep=' ',end='\n',file=none)一般格式
a = 10
print('hello')

print(chr(86))  #

fp = open('test.txt', 'w')  #打开文件，w=write
print('hello', file=fp)  #写入文件
fp.close()  #文件关闭

print('hello', end='-->')  #更改结尾
print('world')

print('hello' + 'world')  #'+'连接字符串

print('1', '2', '3', sep=',')  #sep可以修改多个值之间的分隔符
