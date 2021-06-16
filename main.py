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

pygame.display.set_caption('Snake')
#VARIABLES
bg_color = 0, 0, 0
color_yellow = 255, 255, 0
color_aqua = 0, 200, 255
game_fps = 20
rect_width = 10
s_direction = "r"
s2_direction = "r"
menuList = ['1 Player', '2 Players', 'Settings', 'Quit Game']

snake_color1 = 0, 255, 0
snake_color2 = 0, 0, 255
#CLASSES

f = Food()

#FUNCTIONS
def collision(someRect, objRect):
    return(pygame.Rect(someRect.x, someRect.y, someRect.width, someRect.width).colliderect(objRect))

def text(text, x, y, color, size):
    myfont = pygame.font.SysFont('Arial', size)
    textsurface = myfont.render(str(text), False, color)
    screen.blit(textsurface, (x, y))

f.randomize(WIDTH, HEIGHT)
# int(input("1 or 2 players ?: "))
    

#MAIN CYCLE
main_cycle = True
menu = True
item = 0
while main_cycle:

    # MENU

    while menu:
        pygame.display.update()
        for i, elem in enumerate(menuList):
            if item == i:
                color = color_yellow
            else:
                color = color_aqua
            text(elem, 50, i*150 + 20, color, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #game_over = True
                game_over = True
                menu = False
                screen.fill(color_background)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and item > 0:
                    item -= 1
                if event.key == pygame.K_DOWN and item < len(menuList) - 1:
                    item += 1
                if event.key == pygame.K_RETURN:
                    if item == menuList.index('1 Player'):
                        s = Snake(100, 400, snake_color1)
                        s_direction = "r"
                        player_count = 1
                        menu = False
                    if item == menuList.index('2 Players'):
                        s = Snake(100, 400, snake_color1)
                        s2 = Snake(100, 100, snake_color2)
                        s_direction = "r"
                        s2_direction = "r"
                        player_count = 2
                        menu = False
                    if item == menuList.index('Quit Game'):
                        print('quit')
                        main_cycle = False
                        menu = False
                        break
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
            if player_count == 2:
                if event.key == pygame.K_w:
                    s2_direction = "u"
                if event.key == pygame.K_s:
                    s2_direction = "d"
                if event.key == pygame.K_a:
                    s2_direction = "l"
                if event.key == pygame.K_d:
                    s2_direction = "r"

    #MOVEMENT
    if s_direction == "l":
        s.move(-1, 0)
    if s_direction == "r":
        s.move(1, 0)
    if s_direction == "u":
        s.move(0, -1)
    if s_direction == "d":
        s.move(0, 1)

    if player_count == 2:
        if s2_direction == "l":
            s2.move(-1, 0)
        if s2_direction == "r":
            s2.move(1, 0)
        if s2_direction == "u":
            s2.move(0, -1)
        if s2_direction == "d":
            s2.move(0, 1)

    #RECT VARIABLES
    s_rect = pygame.Rect(s.x, s.y, s.width, s.width)
    if player_count == 2:
        s2_rect = pygame.Rect(s2.x, s2.y, s2.width, s2.width)
    f_rect = pygame.Rect(f.x, f.y, f.width, f.width)
    
    #DRAW
    s.children_list.insert(0, s.pos)
    if s.children <= len(s.children_list):
        s.children_list.pop()
    for each in s.children_list:
        i = s.children_list.index(each)
        Rect = s.children_list[i]
        s.draw(screen, Rect[0], Rect[1])
    if player_count == 2:
        s2.children_list.insert(0, s2.pos)
        if s2.children <= len(s2.children_list):
            s2.children_list.pop()
        for each in s2.children_list:
            i = s2.children_list.index(each)
            Rect = s2.children_list[i]
            s2.draw(screen, Rect[0], Rect[1])

    f.draw(screen)

    #FOOD EAT
    if collision(f_rect, s_rect):
        f.randomize(WIDTH, HEIGHT)
        s.children += 1
        if s.children > 40:
            s.children += 3
        elif s.children > 15:
            s.children += 2

    if player_count == 2:
        if collision(f_rect, s2_rect):
            f.randomize(WIDTH, HEIGHT)
            s2.children += 1
            if s2.children > 40:
                s2.children += 3
            elif s2.children > 15:
                s2.children += 2
        

    #GAMEOVER
    if s.x < 0 or s.x > WIDTH or s.y < 0 or s.y > HEIGHT:
        if player_count == 2:
            print("Player 2 won.")
        print("You lost.")
        menu = True
    if player_count == 2:
        if s2.x < 0 or s2.x > WIDTH or s2.y < 0 or s2.y > HEIGHT:
            print("Player 1 won.")
            menu = True

    for each in s.children_list:
        rect_count = s.children_list.count(each)
        if rect_count != 1:
            menu = True
    if player_count == 2:
        for each in s2.children_list:
            rect_count = s2.children_list.count(each)
            if rect_count != 1:
                menu = True
            
    #UPDATES
    pygame.display.update()
    screen.fill(bg_color)
    time.sleep(1/game_fps)

if player_count == 2:
    print("Player1 final score: ", s.children - 10)
    print("Player2 final score: ", s2.children - 10)
    if s.children > s2.children:
        print("Player1 won.")
    else:
        print("Player2 won.")
pygame.display.quit()
pygame.quit()
