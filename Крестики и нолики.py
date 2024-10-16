import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 800
LINE_WIDTH = 15
BOARD_SIZE = 3
SPACE = WIDTH // BOARD_SIZE
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (255, 255, 255)
CROSS_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-Нолики')
board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
player = 'X'
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SPACE), (WIDTH, SPACE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SPACE * 2), (WIDTH, SPACE * 2), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SPACE, 0), (SPACE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SPACE * 2, 0), (SPACE * 2, HEIGHT), LINE_WIDTH)
def draw_figures():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SPACE + 30, row * SPACE + 30),
                                 (col * SPACE + SPACE - 30, row * SPACE + SPACE - 30), LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SPACE + SPACE - 30, row * SPACE + 30),
                                 (col * SPACE + 30, row * SPACE + SPACE - 30), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SPACE + SPACE // 2, row * SPACE + SPACE // 2),
                                   SPACE // 2 - 30, LINE_WIDTH)
def mark_square(row, col):
    global player
    if board[row][col] is None:
        board[row][col] = player
        player = 'O' if player == 'X' else 'X'
def reset_game():
    global board, player
    board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    player = 'X'
def check_win():
    for row in range(BOARD_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != None:
            print(f"Выйграл {board[row][0]}!")
            return True
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != None:
            print(f"Выйграл {board[0][col]}!")
            return True
    if board[0][0] == board[1][1] == board[2][2] != None:
        print(f"Выйграл {board[0][0]}!")
        return True
    if board[0][2] == board[1][1] == board[2][0] != None:
        print(f"Выйграл {board[0][2]}!")
        return True
    return False
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // SPACE
                clicked_col = mouseX // SPACE
                mark_square(clicked_row, clicked_col)
                if check_win():
                    reset_game()
def check_draw():
        for row in range(BOARD_SIZE):
            if board[row][0] == board[row][1] == board[row][2] != None:
                print(f"ничья {board[row][0]}!")
                return True
        for col in range(BOARD_SIZE):
            if board[0][col] == board[1][col] == board[2][col] != None:
                 print(f"ничья {board[0][col]}!")
                return True
        if board[0][0] == board[1][1] == board[2][2] != None:
            print(f"ничья {board[0][0]}!")
            return True
        if board[0][2] == board[1][1] == board[2][0] != None:
            print(f"ничья {board[0][2]}!")
            return True
        return False
def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    clicked_row = mouseY // SPACE
                    clicked_col = mouseX // SPACE
                    mark_square(clicked_row, clicked_col)
                    if check_win():
                        reset_game()
screen.fill(BACKGROUND_COLOR)
draw_lines()
draw_figures()
pygame.display.update()
if __name__ == "__main__":
    main()