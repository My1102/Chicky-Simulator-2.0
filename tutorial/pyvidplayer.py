#I learn how to play a video in pygame

import pygame
import os
from pyvidplayer2 import Video


# 创建视频对象

FFMPEG_PATH = 'ffmpeg-7.0/bin'

os.environ['PATH'] += os.pathsep + FFMPEG_PATH

vid = Video('graphic/onegold.mp4')

win = pygame.display.set_mode((900,700))
pygame.display.set_caption('Chicky Simulator - Wish')


while vid.active:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vid.stop()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
    
    if key == "r":
        vid.restart()           # 重播视频到开头
    elif key == "p":
        vid.toggle_pause()      # 暂停/播放视频
    elif key == "m":
        vid.toggle_mute()       # 静音/取消静音视频
    elif key == "right":
        vid.seek(15)            # 跳过视频中的15秒
    elif key == "left":
        vid.seek(-15)           # 倒回视频中的15秒
    elif key == "up":
        vid.set_volume(1.0)     # 最大音量
    elif key == "down":
        vid.set_volume(0.0)     # 最小音量
    elif key == "1":
        vid.set_speed(1.0)      # 正常播放速度
    elif key == "2":
        vid.set_speed(2.0)      # 倍速播放视频

    # 只绘制新帧，并且只在绘制了内容时更新屏幕
    
    if vid.draw(win, (-310, 0), force_draw=False):
        pygame.display.update()

    pygame.time.wait(16) # 大约60帧每秒


# 完成后关闭视频

vid.close()
pygame.quit()