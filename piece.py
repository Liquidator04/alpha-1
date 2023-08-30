from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def set_legal_moves(i,j):
        pass

# color should be B or W
class knight(Piece):
    def set_legal_moves(self, i, j, b, color):
        board=b.board
        li=[[i+2,j-1],[i-2,j-1],[i-1,j-2],[i+1,j-2],[i+2,j+1],[i-2,j+1],[i-1,j+2],[i+1,j+2]]  
        moves=[]
        for index in li:
            if index[0]>7 or index[0]<0 or index[1]>7 or index[1]<0:
                continue
            if board[index[0]][index[1]]!=0 and board[index[0]][index[1]].startswith(color):
                continue
            moves.append(index)
        return moves
      
class bishop(Piece):
    def set_legal_moves(self, i, j, b, color):
        board=b.board
        moves=[]
        # top left diagonal
        a,b=i-1,j-1
        while(a>=0 and b>=0 and board[a][b]==0):
            moves.append([a,b])
            a-=1
            b-=1
        else:
            if a>=0 and b>=0 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        # top right diagonal
        a,b=i-1,j+1
        while(a>=0 and b<8 and board[a][b]==0):
            moves.append([a,b])
            a-=1
            b+=1
        else:
            if a>=0 and b<8 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        # bottom left diagonal
        a,b=i+1,j-1
        while(a<8 and b>=0 and board[a][b]==0):
            moves.append([a,b])
            a+=1
            b-=1
        else:
            if a<8 and b>=0 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        # bottom right diagonal
        a,b=i+1,j+1
        while(a<8 and b<8 and board[a][b]==0):
            moves.append([a,b])
            a+=1
            b+=1
        else:
            if a<8 and b<8 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        return moves
    
class pawn(Piece):
    def set_legal_moves(self, i, j, b, color):
        board=b.board
        moves=[]
        if color==b.color:
            if i-1>=0:
                if board[i-1][j]==0:
                    moves.append([i-1, j])
                    if i==6 and board[i-2][j]==0:
                        moves.append([i-2, j])
                if j-1>=0 and type(board[i-1][j-1])==type("") and not board[i-1][j-1].startswith(color):
                    moves.append([i-1, j-1])
                if j+1<8 and type(board[i-1][j+1])==type("") and not board[i-1][j+1].startswith(color):
                    moves.append([i-1, j+1])
        else:
            if i+1<8:
                if board[i+1][j]==0:
                    moves.append([i+1, j])
                    if i==1 and board[i+2][j]==0:
                        moves.append([i+2, j])
                if j-1>=0 and type(board[i+1][j-1])==type("") and not board[i+1][j-1].startswith(color):
                    moves.append([i+1, j-1])
                if j+1<8 and type(board[i+1][j+1])==type("") and not board[i+1][j+1].startswith(color):
                    moves.append([i+1, j+1])      
        return moves