import pygame
class Promotion():
    def __init__(self, color):
        self.color=color
    def Promotion_game(self):
        HEIGHT, WIDTH = 240 , 60

        pygame.init()
        flags = pygame.NOFRAME
        screen = pygame.display.set_mode((HEIGHT, WIDTH),flags = flags)
        clock = pygame.time.Clock()
        running = True

        # background = pygame.Rect((0,0),(HEIGHT, WIDTH))
        # pygame.draw.rect(screen,(150,75, 0),background)
        obj = pygame.image.load("Images/wooden background.jpeg")
        obj = pygame.transform.scale(obj,(HEIGHT,WIDTH))
        screen.blit(obj,(0,0))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0]>=0 and pos[0]<=HEIGHT and pos[1]>=0 and pos[1]<=WIDTH:
                        pieces=["queen", "rook", "knight" , "bishop"]
                        index = int(pos[0]/60)
                        running = False
                        return pieces[index]
            draw(screen, self.color)
            pygame.display.flip()
            clock.tick(60)
        return None
def draw(screen, color):
        pieces=["queen", "rook", "knight" , "bishop"]
        index=0
        for piece in pieces:
            path = "Images/"+color+" "+piece+".png"
            obj = pygame.image.load(path)
            obj = pygame.transform.scale(obj,(60,60))
            screen.blit(obj,(index*60,0))
            index+=1