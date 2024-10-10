import pygame
import time
import random as rnd 

pygame.init()


def message(msg, clr):
    mesg = font_style.render(msg, True, clr)
    font_style = pygame.font.SysFont(None, 20)
    dis.blit(mesg, [width/10, height/2])

def message(msg, clr,x ,y, counter, size):
    font_style = pygame.font.SysFont(None, 40)
    msg += str(counter)
    mesg = font_style.render(msg, True, clr)
    dis.blit(mesg, [x, y])

def draw_snake(snake_bloke, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, ((243, 231, 135)), [i[0],i[1], snake_bloke, snake_bloke])

height = 800
width = 800
yelow = (26, 222, 229)
pink = (255, 123, 196)
b = (153, 153, 0)

x1 = 300
y1 = 300

snake_block = 10
speed = 10

dis = pygame.display.set_mode((height,width)) 
clock = pygame.time.Clock()
pygame.display.set_caption("snake")

def gameLoop():
    game_over = False
    game_close = False

    x1 = height / 2
    y1 = width / 2
    x1_change = 0
    y1_change = 0
    score = 0
    apple_x = round(rnd.randrange(0,width - snake_block)/10)*10
    apple_y = round(rnd.randrange(0,height - snake_block)/10)*10
    apple_x2 = round(rnd.randrange(0,width - snake_block)/10)*10
    apple_y2 = round(rnd.randrange(0,height - snake_block)/10)*10
    apple_x3 = round(rnd.randrange(0,width - snake_block)/10)*10
    apple_y3 = round(rnd.randrange(0,height - snake_block)/10)*10
    apple_x4 = round(rnd.randrange(0,width - snake_block)/10)*10
    apple_y4 = round(rnd.randrange(0,height - snake_block)/10)*10
    apple_x5 = round(rnd.randrange(0,width - snake_block)/10)*10
    apple_y5 = round(rnd.randrange(0,height - snake_block)/10)*10
    apple_block = 10

    snake_list = []
    lenght_of_snake = 1

    while not game_over:
        while game_close:
            dis.fill((153, 51, 255))
            a = ':('
            message('You lost! Press Q to quit or R to restart', b, width/5,height/2, a, 20)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            # print(event)
            
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -speed
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = speed
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -speed
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = speed

        x1 += x1_change
        y1 += y1_change

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        if x1 == apple_x and y1 == apple_y:
            print('СЪЕЛ')
                       
        dis.fill(pink)
        
        message(f'Score:', ((26, 222, 229)), 600, 50, score ,20)
        pygame.draw.rect(dis, (yelow),
                         [apple_x,apple_y,apple_block,apple_block])
        pygame.draw.rect(dis, (yelow),
                         [apple_x2,apple_y2,apple_block,apple_block])
        pygame.draw.rect(dis, (yelow),
                         [apple_x3,apple_y3,apple_block,apple_block])
        pygame.draw.rect(dis, (yelow),
                         [apple_x4,apple_y4,apple_block,apple_block])
        pygame.draw.rect(dis, (yelow),
                         [apple_x5,apple_y5,apple_block,apple_block])
        
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        if (x1 == apple_x and y1 == apple_y) or (x1 == apple_x2 and y1 == apple_y2) or (x1 == apple_x3 and y1 == apple_y3) or (x1 == apple_x4 and y1 == apple_y4) or (x1 == apple_x5 and y1 == apple_y5):
            apple_x = round(rnd.randrange(0,width - snake_block)/10)*10
            apple_y = round(rnd.randrange(0,height - snake_block)/10)*10     
            lenght_of_snake += 1
            score += 1

        draw_snake(snake_block, snake_list)
        pygame.display.update()
        clock.tick(15)

    pygame.quit
    quit()

gameLoop()  