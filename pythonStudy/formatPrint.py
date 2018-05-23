# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'

# 打印格式化与字符串

# 1.如何调整垂直间隔（添加或者删除换行符）
# 2.如何用制表符设置水平间隔
# 3.如何使用格式字符串显示不同的数字格式
# 4.使用格式字符串的两种方法：%符号和format（）方法
# 5.如何使用split()分解字符串和用join()联接字符串
# 6.如何使用startwith()、endwith()、in和index()
# 7.使用strip()去除字符串末尾的部分
# 8.使用upper()和lower()将字符串转化为全大写全小写


# 换行
print("Hello")
print("World")
# 拼接字符串
print("Hello" + "World")
# 增加自己的换行符
print("Hello")
print()
print("World")
# 特殊打印代码 特殊的trld")

# 水平间隔--制表符 制表符的特殊代码是\t
print("ABC\tXYZ")
print("ABCDE\tXYZ")
print("ABCDEF\tXYZ")
print("ABCDEFG\tXYZ")
print("ABCDEFGHI\tXYZ")

# 打印正方形和立方体
print("Number \tSquare \tCube")
for i in range(1, 11):
    print(i, "\t\t", i**2, "\t\t", i**3)

# 两个反斜线打印一个\
print('HI\\WORLD')

# 在字符串中插入变量 %s 表示插入一个字符串变量。如果想插入整数，用%i；想插入浮点数，使用%f
name = "iSara"
print("My name is", name, "and I like you")
print("My name is %s and I like you" % name)
age = 13
print("I am %i years old." % age)
# 数字格式化
dec_number = 12.34567
print("It's %.2f degredds today" % dec_number)  # %.2f 小数点后边显示2位，是四舍五入
number = 12.67
print("%i" % number)  # %d 和 %i 是整数格式化，这里不是四舍五入而是数字会被截断
number1 = 12.3456
print("%e" % number1)
# 自动浮点数 %g 和 %G
number3 = 12.3
number4 = 4567890.123
print("%g" % number3)
print("%g" % number4)
# 打印%
print("I got 90% on my math test")
math = 74.5
print("I got %.1f%% on my math test" % math)
# 多个格式化字符串
English = 60
science = 80.5
print("I got %.1f in English and %.1f in science" % (English, science))
# 存储格式化数字
my_string = "%.2f" % 12.3456
print(my_string)

# 格式化的新方法
print("I got %.1f in English and %.1f in science" % (English, science))
print("I got {0:.1f} in English, {1:.1f} in science" .format(English, science))

# 更多字符串处理
print("cat" + "dog")
# 分解字符串
name_string = "Sam,Sara,Michael,Allen,Tom"
names = name_string.split(",")
print(names)
for name in names:
    print(name)
# join() 联借字符串
word_list = ["My", "name", "is", "iSara"]
long_string = " ".join(word_list)
print(long_string)
long_string = " WOOF ".join(word_list)
print(long_string)
# 搜索字符串
name = "Frankenstein"
print(name.startswith("F"))
print(name.startswith("f"))
print(name.startswith("Frank"))
print(name.endswith("n"))
print(name.endswith("stein"))
print(name.endswith("stone"))

addr1 = "567 Maple Lane"
if "Maple" in addr1:
    position = addr1.index("Maple")
    print("found 'Maple' at index", position)
    print("That address has 'Maple' in it.")
# 删除字符串的一部分
name = "iSara Sun"
short_name = name.strip("un")
print(short_name)

# 改变大小写
string1 = "Hello"
string2 = string1.lower()
string3 = string1.upper()
print(string2)
print(string3)


