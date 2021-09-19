import os
import pygame
from helpers import getX, getY
class Player():
    def __init__(self):
        self.lane = 1 # starts in lane 1
        self.switch_cooldown = 13
        self.position_locked = False
        self.current_frame = 0

        self.moveState = 0 #0 walking 1 left 2 right 3 jump 4 duck


        self.img_width = 2467
        self.img_height = 2162
        self.scale_factor = 5
        self.animations = [[], [], [], [], []]
        for i in range(1, 10):
            self.animations[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pictures', 'player', 'running', 'Walkjumpdown-{}.png'.format(i))), (int(round(self.img_width/self.scale_factor)), int(round(self.img_height/self.scale_factor)))))
        for i in range(34, 44):
            self.animations[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pictures', 'player', 'left', 'Forwardjumpside-to-side-{}.png'.format(i))), (int(round(self.img_width/self.scale_factor)), int(round(self.img_height/self.scale_factor)))))
        for i in range(22, 34):
            self.animations[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pictures', 'player', 'right', 'Forwardjumpside-to-side-{}.png'.format(i))), (int(round(self.img_width/self.scale_factor)), int(round(self.img_height/self.scale_factor)))))
        for i in range(10, 23):
            self.animations[3].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pictures', 'player', 'jump', 'Walkjumpdown-{}.png'.format(i))), (int(round(self.img_width/self.scale_factor)), int(round(self.img_height/self.scale_factor)))))
        for i in range(23, 35):
            self.animations[4].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pictures', 'player', 'duck', 'Walkjumpdown-{}.png'.format(i))), (int(round(self.img_width/self.scale_factor)), int(round(self.img_height/self.scale_factor)))))
    
    def resetAnimation(self):
        self.current_frame = 0
        if(self.moveState == 2):
            if(self.lane < 2):
                self.lane += 1
        self.moveState = 0
    
    def moveLeft(self):
        self.resetAnimation()
        print("MOVE LEFT")
        self.moveState = 1
        self.position_locked = True
        self.switch_cooldown = 13

    def moveRight(self):
        self.resetAnimation()
        print("MOVE RIGHT")
        self.moveState = 2
        self.position_locked = True
        self.switch_cooldown = 13

    def jump(self):
        self.resetAnimation()
        print("JUMP")
        self.moveState = 3
        self.position_locked = True
        self.switch_cooldown = 13
    def duck(self):
        self.resetAnimation()
        print("MOVE RIGHT")
        self.moveState = 4
        self.position_locked = True
        self.switch_cooldown = 13
    def render(self, WIN):  # where to spawn image of player depends on his lane
        offset_x, offset_y = 800/self.scale_factor, 200
        x = [300, 1620/2, 1300]

        if(self.switch_cooldown > 0):
            self.switch_cooldown -= 1
        else:
            self.switch_cooldown = 0
            self.position_locked = False
        
        self.current_frame += 1
        if(self.current_frame % len(self.animations[self.moveState]) == 0):
            self.resetAnimation()
        if(self.moveState == 3):
            offset_y += 200
        WIN.blit(self.animations[self.moveState][self.current_frame], (getX(x[self.lane]) - offset_x, getY(1500) - offset_y))