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
#TCA                     
        main_menu()
        clock.tick(MAX_FPS)
        pygame.display.flip() 
                     
#TCA
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

#TCA
def main_menu():
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 400), 0, 32)
    font = pygame.font.SysFont("impact", 50)
    click = False
    while True:

        screen.fill((0, 0, 0))
        draw_text('Main Menu', font, (255, 255, 0), screen, 87, 35)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(100, 130, 200, 50)
        button_2 = pygame.Rect(100, 230, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                quit_game()
        pygame.draw.rect(screen, (255, 255, 255), button_1)
        pygame.draw.rect(screen, (255, 255, 255), button_2)
        draw_text("Play", font, (0, 0, 0), screen, 160, 122)
        draw_text("Quit", font, (0, 0, 0), screen, 160, 223)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
         
         
def game():
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 400), 0, 32)
    gs = ChessEngine.GameState()
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        drawGameState(screen, gs)
        pygame.display.update()
        mainClock.tick(60)


def quit_game():
    pygame.quit()
    quit()

                     
                     
                     
# TCA
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
