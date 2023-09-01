from abc import ABC, abstractmethod

class Check():
    
        
    # takes a board object b and returns if a king is under check (ans=True/False) and the king which is under check (target="WK"/"BK")
    def check(self, b):
        board = b.board
        ans = False
        for i in range(0, 8):
            for j in range(0, 8):
                piece = board[i][j]
                if type(piece)==type(""):
                    d={'N':knight(), 'B':bishop(), 'P':pawn(), 'R':rook(), 'Q':queen(), 'K':king()}
                    piece_type = d[piece[1]]
                    piece_color = piece[0]
                    legal_moves = piece_type.set_legal_moves(i, j, b, piece_color)
                    for move in legal_moves:
                        row, col = move[0], move[1]
                        target = board[row][col]
                        if type(target)==type("") and target[0]!=piece_color and target[1]=='K':
                            ans = True 
                            break 
                    if ans:
                        break 
            if ans:
                break
        
        return ans,target

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
            if board[index[0]][index[1]]!=0 and str(board[index[0]][index[1]]).startswith(color):
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
    
class rook(Piece):
    
        
    def set_legal_moves(self, i, j, b, color):
        
        board=b.board
        moves=[]
        # above
        a,b=i-1,j
        while(a>=0 and board[a][b]==0):
            moves.append([a,b])
            a-=1
        else:
            if a>=0 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        # below
        a,b=i+1,j
        while(a<8 and board[a][b]==0):
            moves.append([a,b])
            a+=1
        else:
            if a<8 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        # left
        a,b=i,j-1
        while(b>=0 and board[a][b]==0):
            moves.append([a,b])
            b-=1
        else:
            if b>=0 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        # right
        a,b=i,j+1
        while(b<8 and board[a][b]==0):
            moves.append([a,b])
            b+=1
        else:
            if b<8 and type(board[a][b])==type("") and not board[a][b].startswith(color):
                moves.append([a,b])
        
        return moves
    
class queen(Piece):
    
        
    def set_legal_moves(self, i, j, b, color):
        
        board=b.board
        moves=bishop().set_legal_moves(i,j,b,color)+rook().set_legal_moves(i,j,b,color)
        
        return moves

class king(Piece):
    
        
    def set_legal_moves(self, i, j, b, color):
        
        board=b.board
        moves=[[i-1, j], [i-1, j+1], [i, j+1], [i+1, j+1], [i+1, j], [i+1, j-1], [i, j-1], [i-1, j-1]]
        legal_moves=[]
        for move in moves:
            row, col = move[0], move[1]
            if 0<=row<8 and 0<=col<8 and (board[row][col]==0 or not str(board[row][col]).startswith(color)):
                legal_moves.append(move)
        
        return legal_moves

class Pin():
    def pin(self, piece, b, i, j , moves):
        legal_moves=[]
        for move in moves:
            temp=b.board[move[0]][move[1]]
            b.board[move[0]][move[1]]=piece
            b.board[i][j]=0
            var=Check().check(b)
            if not(var[0] and var[1].startswith(piece[0])):
                legal_moves.append(move)
            b.board[move[0]][move[1]]=temp
            b.board[i][j]=piece
        return legal_moves