# TCA
# Main driver file
import pygame
# importing the ChessEngine from the other python code file named  "Chess engine" all stored in the folder named "Chess"
from Chess import ChessEngine
pygame.init()
# Title and Icon
pygame.display.set_caption("Chess")
icon = pygame.image.load('chess.png')
pygame.display.set_icon(icon)

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15   # for animations apparently
IMAGES = {}
def loadImages():
   pieces= ["wp", "wR", "wN","wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
   for piece in pieces:
       IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))

# the main driver for our code which will handle user input and uploading graphics
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerclicks= []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
# VP                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected = ()
                    playerclicks= [] 
                else:
                    sqSelected = (row,col)
                    playerclicks.append(sqSelected)
                if len(playerclicks) == 2:
                    move =ChessEngine.Move(playerclicks[0], playerclicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()
                    playerclicks= []
# TCA
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()

def drawGameState(screen, gs):
     drawBoard(screen)
     drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    # i did not use black as the black pieces wont be visible on the board
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

main()
