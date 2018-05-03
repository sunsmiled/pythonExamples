import pygame
import sys
import math
import random
from pygame.color import THECOLORS

# 画一个[250, 150, 300, 200]、线宽为2的矩形，0表示颜色填满矩形
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])  # 用白色背景填充窗口
# my_list = [250, 150, 300, 200]
# pygame.draw.rect(screen, [255, 0, 0], my_list, 2)   # 画一个圆
# pygame.display.flip()


# 画100个不同大小、不同位置、不同颜色的矩形
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for i in range(100):
#     width = random.randint(0, 255)
#     height = random.randint(0, 100)
#     top = random.randint(0, 400)
#     left = random.randint(0, 500)
#     color_name = random.choice(list(THECOLORS.keys()))
#     color = THECOLORS[color_name]
#     line_width = random.randint(1, 3)
#     pygame.draw.rect(screen, color, [left, top, width, height], line_width)
# pygame.display.flip()

# # #用大量很小的矩形画曲线
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# plotPoints = []
# for x in range(0, 640):
#     y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
#     # pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)
#     plotPoints.append([x, y])
#     pygame.draw.lines(screen, [0, 0, 0], False, plotPoints, 2)
# pygame.display.flip()

# # guess what
# pygame.init()
# dots = [[221, 432], [225, 331], [133, 342], [141, 310],
#         [51, 230], [74, 217], [58, 153], [114, 164],
#         [123, 135], [176, 190], [159, 77], [193, 93],
#         [230, 28], [267, 93], [301, 77], [284, 190],
#         [327, 135], [336, 164], [402, 153], [386, 217],
#         [409, 230], [319, 310], [327, 342], [233, 331],
#         [237, 432]]
# screen = pygame.display.set_mode([640, 480])
# screen.set_at([74, 217], [0, 0, 0])  # 逐点绘制单个像素点
# screen.fill([255, 255, 255])
# pygame.draw.lines(screen, [255, 0, 0], True, dots, 2)


# 显示图片
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("a1.jpg")
# screen.blit(my_ball, [50, 50])
# pygame.display.flip()

# # 移动图片
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("a1.jpg")
# screen.blit(my_ball, [50, 50])
# pygame.display.flip()
# # 加上一下三行代码可以使图片移动
# pygame.time.delay(2000)
# screen.blit(my_ball, [150, 50])
# pygame.draw.rect(screen, [255, 255, 255], [50, 50, 90, 90], 0)  # 这一行“擦掉”第一个球
# pygame.display.flip()

# 流畅的移动图片
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("a1.jpg")
# x = 50
# y = 50
# screen.blit(my_ball, [x, y])
# pygame.display.flip()
# for looper in range(1, 100):
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)  # 这一行“擦掉”第一个球
#     x = x + 5
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()

# # 让图片反弹
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("a1.jpg")
# x = 50
# y = 50
# x_speed = 10
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     if x > screen.get_width() - 90 or x < 0:
#         x_speed = -x_speed
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()

# # 在空间中让图片反弹
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("a1.jpg")
# x = 50
# y = 50
# x_speed = 10
# y_speed = 10
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     y = y + y_speed
#     if x > screen.get_width() - 90 or x < 0:
#         x_speed = -x_speed
#     if y > screen.get_height() - 90 or y < 0:
#         y_speed = -y_speed
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()

# # 利用翻转移动沙滩球图像
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("a1.jpg")
# x = 50
# y = 50
# x_speed = 10
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     if x > screen.get_width():
#         x = 0
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

