# TCA
# Chess Engine

class GameState:
    def __init__(self):
        # board is an 8x8 2d list , each element has 2 characters
        # The first character represents  the colour of the piece black or white
        # The second character represents the type of the piece
        # -- represents an empty space with no piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
# VP        
        self.WhiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        if self.board[move.startrow][move.startcol] != '--':
            self.board[move.startrow][move.startcol] = "--"
            self.board[move.endrow][move.endcol] = move.piecemoved
            self.moveLog.append(move)
            self.WhiteToMove = not self.WhiteToMove

class Move():

    rankstoRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
    rowstoRanks = {v:k for k, v in rankstoRows.items()}

    filestoCol = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
    coltoFiles = {v:k for k, v in filestoCol.items()}

    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]

    def getRankFile(self, r, c):
        return self.coltoFiles[c] + self.rowstoRanks[r]

    def getChessNotation(self):
        return self.getRankFile(self.startrow, self.startcol) + self.getRankFile(self.endrow, self.endcol) 
    
