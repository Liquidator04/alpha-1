class board:
    board=[]
    color=""
    def __init__(self,color):
        self.color=color
        if color=="W":
            self.board.append(['BR','BN','BB','BQ','BK','BB','BN','BR'])
            li=['BP' for _ in range(0,8)]
            self.board.append(li)
            for _ in range(2,6):
                self.board.append([0 for _ in range(0,8)])
            li=['WP' for _ in range(0,8)]
            self.board.append(li)
            self.board.append(['WR','WN','WB','WQ','WK','WB','WN','WR'])
        else:
            li=['WP' for _ in range(0,8)]
            self.board.append(['WR','WN','WB','WK','WQ','WB','WN','WR'])
            self.board.append(li)
            for _ in range(2,6):
                self.board.append([0 for _ in range(0,8)])
            li=['BP' for _ in range(0,8)]
            self.board.append(li)
            self.board.append(['BR','BN','BB','BK','BQ','BB','BN','BR'])


# b=board("BLACK")
# for row in b.board:
#     print(row)