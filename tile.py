class Squares():
    Tiles=[]
    def __init__(self,color):
        
        if color=="B":
            for i in range(0,8):
                files="abcdefgh"
                li=[]
                for j in range(0,8):
                    li.append(files[j]+str(i+1))
                self.Tiles.append(li)
        elif color=="W":
            for i in range(8,0,-1):
                files="abcdefgh"
                li=[]
                for j in range(0,8):
                    li.append(files[j]+str(i))
                self.Tiles.append(li)
    
