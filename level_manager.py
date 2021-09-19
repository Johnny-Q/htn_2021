from obstacle import Obstacle
import pygame
import os
import random
from helpers import HEIGHT, WIDTH, getX, getY, BG_ACC_HEIGHT

class LevelManager:
    #size objects small to start
    def __init__(self):
        self.OBS_WIDTH, self.OBS_HEIGHT = 50, 50
        DISHES = pygame.image.load(os.path.join('Assets', 'pictures',  'obstacles', 'dishes.png'))
        BOOKS = pygame.image.load(os.path.join('Assets', 'pictures', 'obstacles', 'books.png'))
        PIANO = pygame.image.load(os.path.join('Assets', 'pictures', 'obstacles', 'piano.png'))

        self.pos_obstacles = [DISHES, BOOKS, PIANO]
        self.obstacles = []

    def createObstacle(self):
        index = random.randint(0, 2)
        obstacle_image = self.pos_obstacles[index] 
        lane = random.randint(0, 2)
        x = [600, 810, 950]
        obstacle = Obstacle(obstacle_image, getX(x[lane]), getY(652), lane, 1, index == 2)
        # if(lane == 0):
            #Obstacle obj(obstacle_type, lane, img, left_x, left_y, 0)
        #Obstacle obj(obstacle, lane)  #def __init__(self, game_window, img, x, y, lane, depth) -> None:
        self.obstacles.append(obstacle)
        return obstacle


    def update(self, WIN, game_objs):
        for obj in self.obstacles:
            obj.depth += 5
            obj.y += 5
            if obj.lane == 0:
                obj.x += 7*(25-739)/(2160-652)
            if obj.lane == 2:
                obj.x += 10*(1509-893)/(2160-652)
            #obj.width +=1

            #check if object is off screen
            if obj.y >= 1080 - self.OBS_HEIGHT:
                self.obstacles.remove(obj)
                game_objs.remove(obj)
    
    def collisionCheck(self, player):
        for obj in self.obstacles:
            # print(obj.y, getY(BG_ACC_HEIGHT-500))
            if player.lane == obj.lane and getY(BG_ACC_HEIGHT - 1000) <= obj.y and obj.y <= getY(BG_ACC_HEIGHT - 990):
                if obj.isPiano and player.moveState==4: 
                    return False    
                if player.moveState == 3 and not obj.isPiano: #allow jump over objects
                    return False
                print('collision')
                return True
        return False



