import pygame
from board import board
from piece import *
from tile import Squares
# FRONT END FILE
color="W"
b=board(color)
board=[]

Game=[]
# print(b.board)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption('Alpha-1')
clock = pygame.time.Clock()
running = True

TurnChecker=1

def get_board():
    return b.board

# takes a legal set of moves and changes those tiles on the board from 0 to 1 or from WN to WN1
def update_board(moves):
    for move in moves:
        if b.board[move[0]][move[1]]==0:
            b.board[move[0]][move[1]]=1
        else:
            b.board[move[0]][move[1]]=b.board[move[0]][move[1]]+"1"

# removes the trailing 1 from any tiles on the board (which represents a legal move)
def reset_board():
    for i in range(0,8):
        for j in range(0,8):
            if b.board[i][j]==1:
                b.board[i][j]=0
            if type(b.board[i][j])==type("") and b.board[i][j].endswith('1'):
                b.board[i][j]=b.board[i][j][:-1]

# removes the trailing e (which represents that a pawn can be en-passant-ed) from all pawns which are NOT color c (W/B)
def removeEnPassant(c):
    for i in range(0,8):
        for j in range(0,8):
            if type(b.board[i][j])==type("") and b.board[i][j][0]!=c and b.board[i][j][1:]=='P'+'e':
                b.board[i][j]=b.board[i][j][:-1]

piece_selected=''
piece_selected_location=(-1,-1)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            i=int(pos[1]/60)
            j=int(pos[0]/60)
            # print(f"i={i}, j={j}")
            if b.board[i][j]==1:
                promotion=False
                en_passant_capture=False
                castling=False
                if piece_selected[1]=='P' :
                    # print("Entered if")
                    # print(f"{piece_selected} and {color} and {i}")
                    if ((piece_selected.startswith('W') and ((color=='W' and i==0) or (color=='B' and i==7))) or (piece_selected.startswith('B') and ((color=='W' and i==7) or (color=='B' and i==0)))):
                        piece=input("Enter what piece you want to promote to:")
                        piece_selected=(piece_selected[0]+piece).upper()
                        promotion=True
                    elif ((piece_selected.startswith('W') and ((color=='W' and i==4 and piece_selected_location[0]==6) or (color=='B' and i==3 and piece_selected_location[0]==1))) or (piece_selected.startswith('B') and ((color=='W' and i==3 and piece_selected_location[0]==1) or (color=='B' and i==4 and piece_selected_location[0]==6)))):
                        piece_selected+="e"     # represents that this pawn can be captured by en-passant
                    elif j != piece_selected_location[1]:   # pawn is moving to another file without doing captures
                        b.board[piece_selected_location[0]][j]=0    # removing the en-passant-ed pawn
                        en_passant_capture=True
                elif piece_selected[1] in ('R', 'K'):
                    piece_selected+='m'     # represents that piece has been moved and can't be castled anymore
                if piece_selected[1]=='K':
                    if (j-piece_selected_location[1])==-2:  # queen side castling
                        b.board[i][0], b.board[i][3] = b.board[i][3], b.board[i][0]+'m'
                        castling="queen side"
                    elif (j-piece_selected_location[1])==2:  # king side castling
                        b.board[i][5], b.board[i][7] = b.board[i][7]+'m', b.board[i][5]
                        castling="king side"
                b.board[i][j]=piece_selected
                b.board[piece_selected_location[0]][piece_selected_location[1]]=0
                if piece_selected[1]=='P':
                    if not en_passant_capture:
                        notation=Squares(color).Tiles[i][j]
                    else:
                        notation=Squares(color).Tiles[piece_selected_location[0]][piece_selected_location[1]][0]+'x'+Squares(color).Tiles[i][j]+"e.p."
                else:
                    if promotion:
                        notation=Squares(color).Tiles[i][j]+"="+piece_selected[1]
                    elif castling=="queen side":
                        notation="O-O-O"
                    elif castling=="king side":
                        notation="O-O"
                    else:
                        notation=piece_selected[1]+Squares(color).Tiles[i][j]
                TurnChecker*=-1
                reset_board()
                removeEnPassant(piece_selected[0])
                var = Check().check_mate(b)
                if var[0]:
                    notation+="#"
                    Game.append(notation)
                    print(Game)
                    if var[1].startswith('W'):
                        print("Black has won!! White has been checkmated!")
                    else:
                        print("White has won!! Black has been checkmated!")
                    break
                if Check().check(b)[0]:
                    notation+="+"
                Game.append(notation)
                print(Game)
                piece_selected=''
                piece_selected_location=(-1,-1)
            elif type(b.board[i][j])==type("") and b.board[i][j].endswith("1"):
                promotion=False
                if piece_selected[1]=='P' :
                    # print("Entered if")
                    # print(f"{piece_selected} and {i}")
                    if ((piece_selected.startswith('W') and ((color=='W' and i==0) or (color=='B' and i==7))) or (piece_selected.startswith('B') and ((color=='W' and i==7) or (color=='B' and i==0)))):
                        piece=input("Enter what piece you want to promote to:")
                        piece_selected=(piece_selected[0]+piece).upper()
                        promotion=True
                elif piece_selected[1] in ('R', 'K'):
                    piece_selected+='m'     # represents that piece has been moved and can't be castled anymore
                b.board[i][j]=piece_selected
                b.board[piece_selected_location[0]][piece_selected_location[1]]=0
                if piece_selected[1]=='P':
                    notation=Squares(color).Tiles[piece_selected_location[0]][piece_selected_location[1]][0]+"x"+Squares(color).Tiles[i][j]
                else:
                    if promotion:
                        notation=Squares(color).Tiles[piece_selected_location[0]][piece_selected_location[1]][0]+"x"+Squares(color).Tiles[i][j]+"="+piece_selected[1]
                    else:
                        notation=piece_selected[1]+"x"+Squares(color).Tiles[i][j]
                TurnChecker*=-1
                reset_board()
                removeEnPassant(piece_selected[0])
                var = Check().check_mate(b)
                if var[0]:
                    notation+="#"
                    Game.append(notation)
                    print(Game)
                    if var[1].startswith('W'):
                        print("Black has won!! White has been checkmated!")
                    else:
                        print("White has won!! Black has been checkmated!")
                    break
                if Check().check(b)[0]:
                    notation+="+"
                Game.append(notation)
                print(Game)
                piece_selected=''
                piece_selected_location=(-1,-1)
            elif b.board[i][j]==0:
                reset_board()
                piece_selected=''
                piece_selected_location=(-1,-1)
            elif b.board[i][j]=='WN' and TurnChecker==1:
                piece_selected='WN'
                piece_selected_location=(i,j)
                reset_board()
                moves=knight().set_legal_moves(i,j,b,'W')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j]=='BN' and TurnChecker==-1:
                piece_selected='BN'
                piece_selected_location=(i,j)
                reset_board()
                moves=knight().set_legal_moves(i,j,b,'B')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j]=='WB' and TurnChecker==1:
                piece_selected='WB'
                piece_selected_location=(i,j)
                reset_board()
                moves=bishop().set_legal_moves(i,j,b,'W')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j]=='BB' and TurnChecker==-1:
                piece_selected='BB'
                piece_selected_location=(i,j)
                reset_board()
                moves=bishop().set_legal_moves(i,j,b,'B')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j]=='WP' and TurnChecker==1:
                piece_selected='WP'
                piece_selected_location=(i,j)
                reset_board()
                moves=pawn().set_legal_moves(i,j,b,'W')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j]=='BP' and TurnChecker==-1:
                piece_selected='BP'
                piece_selected_location=(i,j)
                reset_board()
                moves=pawn().set_legal_moves(i,j,b,'B')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j].startswith('WR') and TurnChecker==1:
                piece_selected=b.board[i][j]
                piece_selected_location=(i,j)
                reset_board()
                moves=rook().set_legal_moves(i,j,b,'W')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j].startswith('BR') and TurnChecker==-1:
                piece_selected=b.board[i][j]
                piece_selected_location=(i,j)
                reset_board()
                moves=rook().set_legal_moves(i,j,b,'B')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j]=='WQ' and TurnChecker==1:
                piece_selected='WQ'
                piece_selected_location=(i,j)
                reset_board()
                moves=queen().set_legal_moves(i,j,b,'W')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j]=='BQ' and TurnChecker==-1:
                piece_selected='BQ'
                piece_selected_location=(i,j)
                reset_board()
                moves=queen().set_legal_moves(i,j,b,'B')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j].startswith('WK') and TurnChecker==1:
                piece_selected=b.board[i][j]
                piece_selected_location=(i,j)
                reset_board()
                moves=king().set_legal_moves(i,j,b,'W')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)
            elif b.board[i][j].startswith('BK') and TurnChecker==-1:
                piece_selected=b.board[i][j]
                piece_selected_location=(i,j)
                reset_board()
                moves=king().set_legal_moves(i,j,b,'B')
                moves=Pin().pin(piece_selected,b,i,j,moves)
                update_board(moves)

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
                pygame.draw.rect(screen,(150,75, 0),Tile)
            else:
                pygame.draw.rect(screen,(255,255,255),Tile)
            k*=-1
        k*=-1
        board.append(li)
    capturing_location=(-1,-1)
    for i in range(0,8):
        for j in range(0,8):
            checker=False
            checker_legal=False
            if type(b.board[j][i])==type(5):
                if b.board[j][i]==1:
                    piece=pygame.image.load('Images/legal moves.png')
                    checker_legal=True
                    piece = pygame.transform.scale(piece,(30,30))
                    screen.blit(piece,(i*60+15,j*60+15))
            elif type(b.board[j][i])==type(""):
                if b.board[j][i].startswith('WP'):
                    # print("i=",i)
                    # print("j=",j) 
                    piece=pygame.image.load('Images/white pawn.png')
                    checker=True
                if b.board[j][i].startswith('WR'):
                    piece=pygame.image.load('Images/white rook.png')
                    checker=True
                if b.board[j][i].startswith('WN'):
                    piece=pygame.image.load('Images/white knight.png')
                    checker=True
                if b.board[j][i].startswith('WB'):
                    piece=pygame.image.load('Images/white bishop.png')
                    checker=True
                if b.board[j][i].startswith('WQ'):
                    piece=pygame.image.load('Images/white queen.png')
                    checker=True
                if b.board[j][i].startswith('WK'):
                    piece=pygame.image.load('Images/white king.png')
                    checker=True
                if b.board[j][i].startswith('BP'):
                    piece=pygame.image.load('Images/black pawn.png')
                    checker=True
                if b.board[j][i].startswith('BN'):
                    piece=pygame.image.load('Images/black knight.png')
                    checker=True
                if b.board[j][i].startswith('BR'):
                    piece=pygame.image.load('Images/black rook.png')
                    checker=True
                if b.board[j][i].startswith('BB'):
                    piece=pygame.image.load('Images/black bishop.png')
                    checker=True
                if b.board[j][i].startswith('BQ'):
                    piece=pygame.image.load('Images/black queen.png')
                    checker=True
                if b.board[j][i].startswith('BK'):
                    piece=pygame.image.load('Images/black king.png')
                    checker=True
                if checker:
                    piece = pygame.transform.scale(piece,(60,60))
                    screen.blit(piece,(i*60,j*60))
                if b.board[j][i].endswith('1'):
                    piece=pygame.image.load('Images/legal moves.png')
                    piece = pygame.transform.scale(piece,(30,30))
                    screen.blit(piece,(i*60+15,j*60+15))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
