#coding:utf-8

import pygame
import time
import sys
from pygame.locals import *
import random

# 所有的基类
class BaseObject(object):
    def __init__(self, temp_screen, x, y, image):
        super(BaseObject, self).__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.screen = temp_screen

    def move(self, _x=0, _y=0):
        self.x += _x
        self.y += _y


# 飞机的基类
class BasePlane(BaseObject):
    def __init__(self, temp_screen, x, y, image):
        super(BasePlane, self).__init__(temp_screen, x, y, image)
        self.bullets = []

    def display(self, bullet_move_speed):
        self.screen.blit(self.image, (self.x, self.y))
        remove_bullets =[]
        for temp_bullet in self.bullets:
            temp_bullet.display()
            temp_bullet.move(0, bullet_move_speed)
            if temp_bullet.out_of_screen() == True:
                remove_bullets.append(temp_bullet)
        for temp_bullet in remove_bullets:
            self.bullets.remove(temp_bullet)


# 子弹的基类
class BaseBullet(BaseObject):
    """子弹的基类"""
    def __init__(self, temp_screen, x, y, image):
        super(BaseBullet, self).__init__(temp_screen, x, y, image)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
 
    def out_of_screen(self):
        pass 

# 玩家飞机
class HeroPlane(BasePlane):
    def __init__(self, temp_screen):
        super(HeroPlane,self).__init__(temp_screen, 160, 620, "./images/hero1.png")
        self.last_fire_time = 0.00

    def fire(self):
        time_ = time.time()
        if time_ - self.last_fire_time > 0.2:
            self.bullets.append(Bullet(self.screen, self.x+39, self.y-23))
            self.last_fire_time = time_

# 敌军的飞机
class EnemyPlane(BasePlane):
    def __init__(self, temp_screen):
        super().__init__(temp_screen, random.randint(10,370), 5, "./images/enemy1.png")
        self.direction = "right"

    def auto_move(self):
        if self.direction == "right":
            self.x += 4
        else:
            self.x -= 4
        if self.x > 425:
            self.direction = "left"
        elif self.x < 3:
            self.direction = "right"
    def auto_fire(self):
        if random.randint(1,100) < 5:
            self.bullets.append(EnemyBullet(self.screen, self.x+25, self.y+40))


#  玩家的子弹
class Bullet(BaseBullet):
    def __init__(self, temp_screen, _x, _y):
        super(Bullet, self).__init__(temp_screen, _x, _y, "./images/bullet.png")

    def out_of_screen(self):
        if self.y < 0:
            return True
        else:
            return False

# 敌军的子弹
class EnemyBullet(BaseBullet):
    def __init__(self, temp_screen, _x, _y):
        super(EnemyBullet, self).__init__(temp_screen, _x, _y, "./images/bullet1.png")

    def out_of_screen(self):
        if self.y > 730:
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
        hero.display(-15)
        enemy.display(10)
        enemy.auto_move()
        enemy.auto_fire()
        pygame.display.update()
        # 延时，减少cpu负担
        time.sleep(0.01)
        # 事件
        key_control(hero)

if __name__ == "__main__":
    main()