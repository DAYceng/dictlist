import re

# 1，用字符串本身的replace方法:
print('=======replace()替换=======')
a1 = 'Hello world'
b1 = a1.replace('world', 'python')
print('1原始字符串:{}'.format(a1))
print('1替换字符串:{}'.format(b1))

a2 = 'Hello world world world world World'
b2 = a2.replace('world', 'python')
print('2原始字符串:{}'.format(a2))
print('2替换字符串:{}'.format(b2))

a3 = 'Hello world world world world World'
b3 = a3.replace('world', 'python', 2)  # 数字2表示替换2次
print('3原始字符串:{}'.format(a3))
print('3替换字符串:{}'.format(b3))

a4 = 'Hello world world world world World'
b4 = a4.replace('world', 'python', 2).replace('W', 'H').replace(' ', '_')  # replace()可连续使用
print('4原始字符串:{}'.format(a4))
print('4替换字符串:{}'.format(b4))

print('*****替换特殊字符*****')
a5 = 'Hello\world\hello/python:World*Python?555"666<777>888|999OK'
b5 = a5.replace('\\', '_')  # 注意\\表示\
print('5原始字符串:{}'.format(a5))
print('5替换字符串:{}'.format(b5))

b6 = a5.replace('/', '_')
print('6原始字符串:{}'.format(a5))
print('6替换字符串:{}'.format(b6))
b7 = a5.replace(':', '_').replace('"', '_')
print('7原始字符串:{}'.format(a5))
print('7替换字符串:{}'.format(b7))

print('=======正则表达式替换=======')
# 2用正则表达式来完成替换:
c1 = 'hello world'
strinfo = re.compile('world')
d1 = strinfo.sub('python', c1)
print('1原始字符串:{}'.format(c1))
print('1替换字符串:{}'.format(d1))

c2 = 'hello world world world World'
strinfo = re.compile('world')
d2 = strinfo.sub('python', c2, )
print('2原始字符串:{}'.format(c2))
print('2替换字符串:{}'.format(d2))

c2_1 = 'hello world world world World'
strinfo = re.compile('world')
d2_1 = strinfo.sub('python', c2_1, 2)  # 只替换2次
print('2_1原始字符串:{}'.format(c2_1))
print('2_1替换字符串:{}'.format(d2_1))

c2_2 = 'hello world world world World'
strinfo = re.compile('world', re.I)  # re.I 表示忽略大小写
d2_2 = strinfo.sub('python', c2_2)
print('2_2原始字符串:{}'.format(c2_2))
print('2_2替换字符串:{}'.format(d2_2))

print('*****替换特殊字符*****')
c3 = 'Hello-world\hello/python:World*Python?555"666<777>888|999OK'
strinfo = re.compile('[/:*?"<>|\\\\]')  # 注意用4个\\\\来替换\
d3 = strinfo.sub('_', c3)
print('3原始字符串:{}'.format(c3))
print('3替换字符串:{}'.format(d3))

c4 = 'Hello-world\hello/python:World*Python?555"666<777>888|999OK'
strinfo = re.compile(r'[/:*?"<>|\\]')  # 加r,2个\即可
d4 = strinfo.sub('_', c4)
print('4原始字符串:{}'.format(c4))
print('4替换字符串:{}'.format(d4))