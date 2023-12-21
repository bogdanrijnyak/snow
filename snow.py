import pygame
from random import randint
pygame.init()
info = pygame.display.Info()

WIDTH = info.current_w
HEIGHT = info.current_h
FPS=30


window = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
clock = pygame.time.Clock()

snow = []
count = 1000
maxSize = 5

for i in range (count):
    x,y = randint(0,WIDTH), randint(0,HEIGHT)
    size = randint (1, maxSize)
    snow.append([x,y,size])

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    for obj in snow:
        x,y = obj[0], obj[1]
        size = obj[2]
        obj[1]+=obj[2]

        if y > HEIGHT+size:

            obj[0] = randint(0,WIDTH)
            obj[1] = -randint(10,100)

    window.fill(pygame.Color('black'))
    for obj in snow :
        x,y = obj[0], obj[1]
        size = obj[2]
        c = 55 + 200 // maxSize * size
        color = (c,c,c)

        pygame.draw.circle(window,color,(x,y),size)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
# Write your code here :-)
