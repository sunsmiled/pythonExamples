# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'


# # 播放声音
# import pygame
# import sys
# pagame.init()
# pygame.mixer.init()
#
# screen = pygame.display.set_mode([640, 480])
# pygame.time.delay(1000)
# splat = pygame.mixer.Sound("")
# splat.play()
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 播放音乐
import pygame
import sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000)

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

