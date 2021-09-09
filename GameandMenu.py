import pygame, sys
# TCA
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
    screen = pygame.display.set_mode((525, 525), 0, 32)
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
