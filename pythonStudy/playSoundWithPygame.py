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

# # 播放音乐
# import pygame
# import sys
# pygame.init()
# pygame.mixer.init()
#
# screen = pygame.display.set_mode([640, 480])
# pygame.time.delay(1000)
#
# pygame.mixer.music.load("music.mp3")
# pygame.mixer.music.play()
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()


# # 有音量调节的音乐和声音
# import pygame
# import sys
# pygame.mixer.init()
#
# screen = pygame.display.set_mode([640, 480])
# pygame.time.delay(1000)
# pygame.mixer.music.load("music.mp3")
# pygame.mixer.music.set_volume(0.30)    # 调节音乐的音量
# pygame.mixer.music.play()
# splat = pygame.mixer.Sound("splat.wav")
# splat.set_volume(0.50)    # 调节音效的音量
# splat.play()
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 等待歌曲结束
import pygame
import sys
pygame.mixer.init()
screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000)

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.5)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if not pygame.mixer.music.get_busy():
        splat.play()
        pygame.time.delay(1000)
        sys.exit()





