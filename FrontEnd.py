import pygame
from board import board
# FRONT END FILE
b=board("WHITE")
board=[]
print(b.board)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption('Alpha-1')
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
        li=[]
        for j in range(0,8):
            Tile=pygame.Rect((i*60,j*60),(60,60))
            li.append(Tile)
            if k==-1:
                pygame.draw.rect(screen,(0,0,0),Tile)
            else:
                pygame.draw.rect(screen,(255,255,255),Tile)
            k*=-1
        k*=-1
        board.append(li)
    for i in range(0,8):
        for j in range(0,8):
            checker=False
            if b.board[j][i]=='WP':
                # print("i=",i)
                # print("j=",j)
                piece=pygame.image.load('Images/white pawn.png')
                checker=True
            if b.board[j][i]=='WR':
                piece=pygame.image.load('Images/white rook.png')
                checker=True
            if b.board[j][i]=='WN':
                piece=pygame.image.load('Images/white knight.png')
                checker=True
            if b.board[j][i]=='WB':
                piece=pygame.image.load('Images/white bishop.png')
                checker=True
            if b.board[j][i]=='WQ':
                piece=pygame.image.load('Images/white queen.png')
                checker=True
            if b.board[j][i]=='WK':
                piece=pygame.image.load('Images/white king.png')
                checker=True
            if b.board[j][i]=='BP':
                piece=pygame.image.load('Images/black pawn.png')
                checker=True
            if b.board[j][i]=='BN':
                piece=pygame.image.load('Images/black knight.png')
                checker=True
            if b.board[j][i]=='BR':
                piece=pygame.image.load('Images/black rook.png')
                checker=True
            if b.board[j][i]=='BB':
                piece=pygame.image.load('Images/black bishop.png')
                checker=True
            if b.board[j][i]=='BQ':
                piece=pygame.image.load('Images/black queen.png')
                checker=True
            if b.board[j][i]=='BK':
                piece=pygame.image.load('Images/black king.png')
                checker=True
            if checker:
                piece = pygame.transform.scale(piece,(60,60))
                screen.blit(piece,(i*60,j*60))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()