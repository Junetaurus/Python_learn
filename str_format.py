age = 20
name = 'Swaroop'

print('{0} was  {1} years old when he wrote this book'.format(name, age))
print('{} was {} years old when he wrote this book'.format(name, age))

print('Why is {0} playing with that python？'.format(name))
print('Why is {} playing with that python?'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end='')
print('b', end='')
print('c')

print('a', end=' ')
print('b', end=' ')
print('c')

print('This is the first line\nThis is the second line')
# 转义序列
print("This is the first sentence. \
This is the second sentence.")
print("This is the first sentence. This is the second sentence.")

# 原始字符串
print(r"Newlines are indicated by \n")

# 标识符命名
# 第一个字符必须是字母表中的字母(大写 ASCII 字符或小写 ASCII 字符或 Unicode 字 符)或下划线( _ )。
# 标识符的其它部分可以由字符(大写 ASCII 字符或小写 ASCII 字符或 Unicode 字符)、 下划线( _ )、数字(0~9)组成。
# 标识符名称区分大小写。例如， myname 和 myName 并不等同。要注意到前者是小写字 母 n 而后者是大写字母 N 。