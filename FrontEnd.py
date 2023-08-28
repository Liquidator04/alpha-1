import pygame
from board import board
# FRONT END FILE
b=board("WHITE")
print(b.board)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    k=1
    for i in range(0,8):
        for j in range(0,8):
            Tile=pygame.Rect((i*60,j*60),(60,60))
            if k==-1:
                pygame.draw.rect(screen,(0,0,0),Tile)
            else:
                pygame.draw.rect(screen,(255,255,255),Tile)
            k*=-1
        k*=-1
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()