class board:
    board=[]
    def __init__(self,color):
        if color=="WHITE":
            self.board.append(['BR','BN','BB','BQ','BK','BB','BN','BR'])
            li=['BP' for _ in range(0,8)]
            self.board.append(li)
            li=[0 for _ in range(0,8)]
            for _ in range(3,7):
                self.board.append(li)
            li=[]
            li=['WP' for _ in range(0,8)]
            self.board.append(li)
            self.board.append(['WR','WN','WB','WQ','WK','WB','WN','WR'])
        else:
            li=['WP' for _ in range(0,8)]
            self.board.append(['WR','WN','WB','WQ','WK','WB','WN','WR'])
            self.board.append(li)
            li=[0 for _ in range(0,8)]
            for _ in range(3,7):
                self.board.append(li)
            li=[]
            li=['BP' for _ in range(0,8)]
            self.board.append(li)
            self.board.append(['BR','BN','BB','BQ','BK','BB','BN','BR'])


b=board("BLACK")
print(b.board)