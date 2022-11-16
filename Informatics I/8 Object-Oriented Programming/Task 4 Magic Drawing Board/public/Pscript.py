#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):
        #instance check
        if not (isinstance(y,int) and isinstance(x,int)):
            raise Warning("Invalid datatype in constructor")
        
        if x<=0 or y<=0:
            raise Warning("Board invalid size")
        self.__x = x
        self.__y = y
        self.__pic = list()
        for j in range(0,y):
            line = ""
            for i in range(0,x):
                line += "0"
            if j<y-1: line += "\n"
            self.__pic.append(line)
            
    #print pic to console        
    def img(self):
        res=""
        for line in self.__pic:
            res+= line
        print(res)
        return res

    
    
    def pixel(self,coordinate):
        #instance check
        if not (isinstance(coordinate[0],int) and isinstance(coordinate[1],int)):
            raise Warning("Invalid datatype in pixel")
        
        #out of bounds check
        if coordinate[0]<0 or coordinate[0]>=self.__x or coordinate[1]<0 or coordinate[1]>=self.__y:
            raise Warning("x or y out of bound for pixel")
        
        line=list(self.__pic[coordinate[1]])
        line[coordinate[0]] = "1"
        self.__pic[coordinate[1]] = "".join(line)
        return
    
    def rect(self, coord1, coord2):
        #instance check
        if not (isinstance(coord1[0],int) and isinstance(coord1[1],int)):
            raise Warning("Invalid datatype in rect coord1")
            
        #instance check
        if not isinstance(coord2[0],int) and isinstance(coord2[1],int):
            raise Warning("Invalid datatype in rect coord2")
        
        #out of bounds check
        if coord1[0]<0 or coord1[0]>self.__x or coord1[1]<0 or coord1[1]>self.__y:
            raise Warning("x or y out of bound for rect coordinate 1")
        if coord2[0]<0 or coord2[0]>self.__x or coord2[1]<0 or coord2[1]>self.__y:
            raise Warning("x or y out of bound for rect coordinate 2")
        
        #coord1 < coord2:
        if coord1[0]>= coord2[0] or coord1[1]>=coord2[1]:
            raise Warning("Invalid rect inputs: coord1 >= coord2")
            
        
        #coord 1 and 2 are valid
        for y in range(coord1[1],coord2[1]):
            line = list(self.__pic[y])
            for x in range(coord1[0],coord2[0]):
                line[x] = "1"
            self.__pic[y] = "".join(line)

        return
    
    #redraw board
    def reset(self):
        for j in range(0,self.__y):
            line = ""
            for i in range(0,self.__x):
                line += "0"
            if j<self.__y-1: line += "\n"
            self.__pic[j]=line

        return
        
        
            

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6,4)
    db.pixel((5,3))
    db.rect((0,0),(2,2))
    db.img()

