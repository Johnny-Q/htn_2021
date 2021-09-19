#!./Scripts/python.exe
from level_manager import LevelManager
from player import Player
import pygame
from controller import Controller
import random
import os
from helpers import WIDTH, HEIGHT

pygame.init()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BG = pygame.image.load(os.path.join("Assets", "pictures", "bg.png"))
SCORE_FONT = pygame.font.Font(os.path.join("Assets", 'Winkle-Regular.ttf'), 35)
score = 0

game_objs = []

def render():
    WIN.fill((255, 255, 255))
    WIN.blit(pygame.transform.scale(BG, (648, 864)), (0, 0))
    score_text = SCORE_FONT.render("Score: {}".format(score), 1, (0, 0, 0))
    WIN.blit(score_text, (100, 100))
    
    for obj in game_objs:
        obj.render(WIN)

    pygame.display.update()

def main():
    run = True
    controller = Controller()
    clock = pygame.time.Clock()
    player = Player()
    game_objs.append(player)
    level_manager = LevelManager()

    def draw_end(text):
        draw_text = SCORE_FONT.render(text, 1, (0, 0, 0))
        WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
    
    while run:
        clock.tick(60)

        global score
        score += 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #make sure camera is connected
        if controller.cap.isOpened() and not player.position_locked:
            success, image = controller.cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            image = controller.formatImage(image)
            results = controller.pose.process(image)
            if(results.pose_landmarks):
                MOVE = controller.classifyPose(results)
                if(MOVE >= 0):
                    if(MOVE > player.lane):
                        player.moveRight()
                    elif(MOVE < player.lane):
                        player.moveLeft()
                        player.lane = MOVE
                else: #-1 jump, -2 duck
                    if(MOVE == -1):
                        player.jump()
                    elif(MOVE == -2):
                        player.duck()

                
                # if MOVE == "RIGHT":
                #     player.lane = 2
                # elif MOVE == "MIDDLE":
                #     player.lane = 1
                # elif MOVE == "LEFT":
                #     player.lane = 0
            
            controller.renderFeedback(image, results)
        
        #periodically spawn obstacles
        if(random.randint(0, 20) == 0):
            # print("spawning obj")
            game_objs.append(level_manager.createObstacle())

        level_manager.update(WIN, game_objs)
        render()

        #collision checking
        if(level_manager.collisionCheck(player)):
            endText= "Game over! Your score is " + str(score)
            controller.cap.release()
            draw_end(endText)
            return

if __name__ == "__main__":
    main()
