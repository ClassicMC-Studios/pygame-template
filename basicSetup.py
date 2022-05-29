from operator import truediv
import pygame
pygame.init()
display = pygame.display.set_mode((720,480))
pygame.display.set_caption('template')
running = True
px,py = 100,100
def redraw():
    display.fill((255,255,255))
    pygame.draw.rect(display,(0,0,0),pygame.Rect(px,py,100,100))
    pygame.display.flip()
while running:
    redraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        py -= 1
        redraw()
    if keys[pygame.K_DOWN]:
        py += 1
        redraw()
    if keys[pygame.K_LEFT]:
        px -= 1
        redraw()
    if keys[pygame.K_RIGHT]:
        px += 1
        redraw()