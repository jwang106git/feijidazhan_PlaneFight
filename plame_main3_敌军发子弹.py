#coding:utf-8

import pygame
import time
import sys
from pygame.locals import *
import random

class HeroPlane(object):
    def __init__(self, temp_screen):
        self.x = 160
        self.y = 620
        self.image = pygame.image.load("./images/hero1.png")
        self.screen = temp_screen
        self.bullets = []
        self.last_fire_time = 0.00
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        remove_bullets =[]
        for temp_bullet in self.bullets:
            temp_bullet.display()
            temp_bullet.move(0, -15)
            if temp_bullet.out_of_screen() == True:
                remove_bullets.append(temp_bullet)
        for temp_bullet in remove_bullets:
            self.bullets.remove(temp_bullet)

    def move(self, _x=0, _y=0):
        self.x += _x
        self.y += _y

    def fire(self):
        time_ = time.time()
        if time_ - self.last_fire_time > 0.2:
            self.bullets.append(Bullet(self.screen, self.x+39, self.y-23))
            self.last_fire_time = time_

class Bullet(object):
    # 39 -23
    def __init__(self, temp_screen, _x, _y):
        self.x = _x
        self.y = _y
        self.image = pygame.image.load("./images/bullet.png")
        self.screen = temp_screen
    
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, _x=0, _y=0):
        self.x += _x
        self.y += _y 

    def out_of_screen(self):
        if self.y < 0:
            return True
        else:
            return False
# 敌军的飞机
class EnemyPlane(object):
    def __init__(self, temp_screen):
        self.x = random.randint(10,370)
        self.y = 5
        self.image = pygame.image.load("./images/enemy1.png")
        self.screen = temp_screen
        self.bullets = []
        self.direction = "right"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        remove_bullets = []
        for temp_bullet in self.bullets:
            temp_bullet.display()
            temp_bullet.move(0, 10)
            if temp_bullet.out_of_screen() == True:
                remove_bullets.append(temp_bullet)
        for temp_bullet in remove_bullets:
            self.bullets.remove(temp_bullet)
    def move(self, _x=0, _y=0):
        self.x += _x
        self.y += _y

    def auto_move(self):
        if self.direction == "right":
            self.x += 4
        else:
            self.x -= 4
        if self.x > 425:
            self.direction = "left"
        elif self.x < 3:
            self.direction = "right"
        '''
        if self.x > self.x_before:
            self.x_before = self.x
            if self.x < 300:
                self.x += 1
            else:
                self.x -=1
        else:
            self.x_before = self.x
            if self.x > 100:
                self.x -= 1
            else:
                self.x +=1
        '''
    def auto_fire(self):
        if random.randint(1,100) < 5:
            self.bullets.append(EnemyBullet(self.screen, self.x+25, self.y+40))
# 敌军的子弹
class EnemyBullet(object):
    def __init__(self, temp_screen, _x, _y):
        self.x = _x
        self.y = _y
        self.image = pygame.image.load("./images/bullet1.png")
        self.screen = temp_screen
    
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, _x=0, _y=0):
        self.x += _x
        self.y += _y 

    def out_of_screen(self):
        if self.y > 640:
            return True
        else:
            return False


def key_control(hero):
    # 获取事件
    for event in pygame.event.get():
        # 判断事件是否为退出事件
        if event.type == QUIT:
            # 退出pygame
            pygame.quit()
            # 退出系统
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                hero.fire()
            elif event.key == K_a or event.key == K_LEFT:
                hero.move(-10)
            elif event.key == K_d or event.key == K_RIGHT:
                hero.move(10)
            elif event.key == K_w or event.key == K_UP:
                hero.move(0, -20)
            elif event.key == K_s or event.key == K_DOWN:
                hero.move(0, 20)          
            else:
                pass
        else:
            pass

def main():
    # 创建窗口
    pygame.init()
    screen = pygame.display.set_mode((480,752),0,32)
    pygame.display.set_caption('This is my first pygame-program')
    # 背景图片
    background = pygame.image.load("./images/background.png")
    # plane
    hero = HeroPlane(screen)
    # enemy
    enemy = EnemyPlane(screen)
    while True:
        # 刷新屏幕                     
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.auto_move()
        enemy.auto_fire()
        pygame.display.update()
        # 延时，减少cpu负担
        time.sleep(0.01)
        # 事件
        key_control(hero)

if __name__ == "__main__":
    main()