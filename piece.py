from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def set_legal_moves(i,j):
        pass

class knight(Piece):
    def set_legal_moves(self, i, j, board, color):
        li=[[i+2,j-1],[i-2,j-1],[i-1,j-2],[i+1,j-2],[i+2,j+1],[i-2,j+1],[i-1,j+2],[i+1,j+2]]  
        moves=[]
        for index in li:
            if index[0]>7 or index[0]<0 or index[1]>7 or index[1]<0:
                continue
            if board[index[0]][index[1]]!=0 and board[index[0]][index[1]].startswith(color):
                continue
            moves.append(index)
        return moves
