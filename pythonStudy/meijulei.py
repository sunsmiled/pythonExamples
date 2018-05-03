# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'

from enum import Enum, unique
# 枚举类型
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 如果需要更精确的控制枚举类型，可以从Enum派生出自定义类
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon)
print(Weekday.Thu)
print(Weekday.Fri.value)
print(Weekday(1))

