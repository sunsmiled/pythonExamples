
import mymodule
import time
import random
import pygame


celsius = 22.5
fahrenheit = mymodule.c_to_f(celsius)
print("that's", fahrenheit, " degree Fahrenheit")

print("how")
time.sleep(2)
print("are")
time.sleep(2)
print("you")
time.sleep(2)
print("today?")
print(random.randint(0, 100))
print(random.randint(0, 100))
# 随机的小数
print(random.random())
pygame.init()
screen = pygame.display.set_mode([640, 480])
