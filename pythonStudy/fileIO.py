# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'


import pickle

my_file = open('newNote.txt', 'r')
lines = my_file.readlines()
print(lines)

my_file.seek(0)
# 一次只读一行
first_line = my_file.readline()
second_line = my_file.readline()
print(first_line)
print(second_line)
# 回到起始位置
my_file.seek(0)
first_line_again = my_file.readline()
print(first_line_again)

# 使用完文件 记得关闭它
my_file.close()

# 追加到文件
todo_list = open('newNote.txt', 'a')
todo_list.write('\nStudy day by day')
todo_list.close()
todo_list = open('newNote.txt', 'r')

lines_after_append = todo_list.readlines()
print(lines_after_append)
todo_list.close()

# 写文件 (对一个新文件写，即当前目录中还没有这个文件）
new_file = open("my_new_file.txt", 'w')
new_file.write("Study\n")
new_file.write("Play soccer\n")
new_file.write("Go to bed")
new_file.close()
# 写文件 （对一个已有文件写，会覆盖该文件之前的内容）
the_file = open("my_new_file", "w")
the_file.write("Wake up\n")
the_file.write("Watch cartoons\n")
the_file.close()

# 在文件中保存内容：pickle
# 要pickle某个东西，比如列表，需要使用dump()函数
my_list = ['Fred', 73, 'Hello there', 81.9876e-13]
pickle_file = open('my_pickle_list.pkl', 'wb+')
pickle.dump(my_list, pickle_file)
pickle_file.close()
# 去除pickle前的数据
# 使用load()还原
pickle_file1 = open('my_pickle_list.pkl', 'rb')
recovered_list = pickle.load(pickle_file1)
pickle_file.close()

print(recovered_list)



