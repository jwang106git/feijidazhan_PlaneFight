import pygame
import time
import sys
from pygame.locals import *


def main():
    # 创建窗口
    pygame.init()
    screen = pygame.display.set_mode((480,752),0,32)
    pygame.display.set_caption('This is my first pygame-program')
    
    # 背景图片
    background = pygame.image.load("./images/background.png")
    # plane
    hero = pygame.image.load("./images/hero1.png")
    hero_pos = [160,620]
    while True:
        # 刷新屏幕                     
        screen.blit(background, (0,0))
        screen.blit(hero, (hero_pos[0],hero_pos[1]))
        pygame.display.update()
        # 延时，减少cpu负担
        time.sleep(0.05)

        # 获取事件
        for event in pygame.event.get():
            # 判断事件是否为退出事件
            if event.type == QUIT:
                # 退出pygame
                pygame.quit()
                # 退出系统
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    hero_pos[0] -= 1
                elif event.key == K_d or event.key == K_RIGHT:
                    hero_pos[0] += 1
                elif event.key == K_w or event.key == K_UP:
                    hero_pos[1] -= 1
                elif event.key == K_s or event.key == K_DOWN:
                    hero_pos[1] += 1          
                else:
                    pass
            else:
                pass
if __name__ == "__main__":
    main()