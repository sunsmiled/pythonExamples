# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# if __name__ == '__main__':
#     test()
#

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        # self.__score = score
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')



bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


class Animal(object):
    def run(self):
        print ('Animal is running、、、')


class Dog(Animal):

    def run(self):
        print('Dog is running')

    def eat(self):
        print('Eating meat')


class Cat(Animal):
    def run(self):
        print('Cat is running')




































