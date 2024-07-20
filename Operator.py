#+ - * / //(取整) % **(幂运算) = += -= /=  and or not
a, b = 10, 20  #系列解包赋值
print(a, b)
a, b = b, a  #交换a,b的值
print(a, b)

print(8 < 7 and 10 / 0)
print(8 > 7 or 10 / 0)

#位操作 &位与 |位或 ^位异或 ~位取反 <<左移位 >>右移位
print(2 << 2)  #2*2*2
print(8 >> 2)  #8/2/2

num=eval(input('Enter a number: '))
x=num%10
y=num//10%10
z=num//100%10
print('个位',x,'十位',y,'百位',z)