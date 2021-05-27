import time
import pygame
from snake import Snake
from food import Food

#PYGAME INIT
pygame.init()
pygame.font.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#VARIABLES
bg_color = 0, 0, 0
game_fps = 20
rect_width = 10
s_direction = "r"

#CLASSES
s = Snake()
f = Food()

#FUNCTIONS
def collision(someRect, objRect):
    return(pygame.Rect(someRect.x, someRect.y, someRect.width, someRect.width).colliderect(objRect))

#MAIN CYCLE
main_cycle = True
while main_cycle:
    pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_cycle = False
            break

        #KEY PRESSED
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                s_direction = "u"
            if event.key == pygame.K_DOWN:
                s_direction = "d"
            if event.key == pygame.K_LEFT:
                s_direction = "l"
            if event.key == pygame.K_RIGHT:
                s_direction = "r"
            
            if event.key == pygame.K_a:
                s.children += 1
                f.randomize(WIDTH, HEIGHT)

    #MOVEMENT
    if s_direction == "l":
        s.move(-1, 0)
    if s_direction == "r":
        s.move(1, 0)
    if s_direction == "u":
        s.move(0, -1)
    if s_direction == "d":
        s.move(0, 1)

    #RECT VARIABLES
    s_rect = pygame.Rect(s.x, s.y, s.width, s.width)
    f_rect = pygame.Rect(f.x, f.y, f.width, f.width)
    
    #DRAW
    s.children_list.insert(0, s.pos)
    if s.children <= len(s.children_list):
        s.children_list.pop()
    for each in s.children_list:
        i = s.children_list.index(each)
        Rect = s.children_list[i]
        s.draw(screen, Rect[0], Rect[1])

    f.draw(screen)

    #FOOD EAT
    if collision(f_rect, s_rect):
        f.randomize(WIDTH, HEIGHT)
        s.children += 1

    #GAMEOVER
    if s.x < 0 or s.x > WIDTH or s.y < 0 or s.y > HEIGHT:
        main_cycle = False
        break

    for each in s.children_list:
        rect_count = s.children_list.count(each)
        if rect_count != 1:
            main_cycle = False
            break

    #UPDATES
    pygame.display.update()
    screen.fill(bg_color)
    time.sleep(1/game_fps)

pygame.display.quit()
pygame.quit()
