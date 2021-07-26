#CW

#Use this class to create pieces on the board.

class Piece:
    #Initializes the piece with its co-ordinates, name and which player it belongs to.
    def __init__(self,x,y,name,color):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        if self.name is "P":
            self.adjustx,self.adjusty= 15, 10
        elif self.name is "R" or self.name is "K":
            self.adjustx,self.adjusty= 11, 10
        elif self.name is "B":
            self.adjustx,self.adjusty= 5, 10
        elif self.name is "Q" or self.name is "K":
            self.adjustx,self.adjusty= 9, 10
    
    #Function to get piece color and name of piece.
    def getName(self):
        return [self.name, self.color]

    #Returns position of piece on the board (coordinates).
    def getPosition(self):
        return (self.x, self.y)
    
    #Sets the position of a piece. It used when a piece is moved.
    def setPosition(self,x,y):
        self.x=x
        self.y=y

    #It displays the piece on the board    
    def drawPieceAfterMove(self, x, y, color):
        if player is "White":
            player="1"
        else:
            player="2"
        color = "2"
        self.image = load_image('images/' + self.name + '.png')
        self.imagerect = self.image.get_rect()
        self.imagerect.left = x
        self.imagerect.top = y + topMenu
        gameDisplay.blit(self.image, self.imagerect)
