# @uthor: $um@nth Nethi
# Date: 25-07-2022

import pygame

pygame.init()

screen = pygame.display.set_mode((603, 603))
pygame.display.set_caption('SUDOKU')
font = pygame.font.SysFont('Comic Sans MS', 40)

black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
light_white = (220, 220, 220)
red = (255, 0, 0)

board = pygame.Surface((603, 603))
board.fill(black)
running = True
input_flag = 1
sol_flag = 0
input_cords = {}

# Display Board
for i in range(1, 3):
    pygame.draw.rect(board, grey, (0, 201 * i, 603, 7))
    pygame.draw.rect(board, grey, (201 * i, 0, 7, 603))

for i in range(1, 9):
    pygame.draw.rect(board, grey, (0, 67 * i, 603, 1))
    pygame.draw.rect(board, grey, (67 * i, 0, 1, 603))

game = [[None for i in range(9)] for j in range(9)]

# Default Board
game = [
    [7, 5, None, 1, 8, 2, None, None, None],
    [8, 1, None, None, None, 7, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [9, None, None, 2, 5, 8, None, None, 1],
    [1, None, 8, 7, None, 6, None, None, 5],
    [3, None, 5, 9, 1, 4, None, None, 7],
    [5, 8, None, 6, 7, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [6, None, 1, None, None, None, None, None, None]
]


def display_board():
    global input_flag
    screen.blit(board, (0, 0))
    for i in range(9):
        for j in range(9):
            input_cords.setdefault((i, j), red)
            if game[i][j] is not None:
                text = font.render(str(game[i][j]), True, input_cords[(i, j)])
                screen.blit(text, (67 * j + 22, 67 * i + 5))


def check_validity(row, col, num):
    for i in range(9):
        if game[row][i] == num:
            return False
        if game[i][col] == num:
            return False
    for i in range(3):
        for j in range(3):
            if game[row - row % 3 + i][col - col % 3 + j] == num:
                return False
    return True


def solve(i, j):
    global input_flag, game
    if i == 9:
        return True
    if j == 9:
        return solve(i + 1, 0)
    if game[i][j] is not None:
        return solve(i, j + 1)
    for num in range(1, 10):
        if check_validity(i, j, num):
            game[i][j] = num
            input_cords[(i, j)] = green
            display_board()
            pygame.display.update()
            pygame.time.wait(35)
            if solve(i, j + 1):
                return True
            game[i][j] = None
            input_cords[(i, j)] = white
            display_board()
            pygame.display.update()
            pygame.time.wait(35)
    return False


while running:
    screen.fill(black)
    screen.blit(board, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and input_flag:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 67
            y = pos[1] // 67
        if event.type == pygame.KEYDOWN and input_flag:
            if event.key == pygame.K_0:
                game[y][x] = 0
                input_cords[(y, x)] = red
            if event.key == pygame.K_1:
                game[y][x] = 1
                input_cords[(y, x)] = red
            if event.key == pygame.K_2:
                game[y][x] = 2
                input_cords[(y, x)] = red
            if event.key == pygame.K_3:
                game[y][x] = 3
                input_cords[(y, x)] = red
            if event.key == pygame.K_4:
                game[y][x] = 4
                input_cords[(y, x)] = red
            if event.key == pygame.K_5:
                game[y][x] = 5
                input_cords[(y, x)] = red
            if event.key == pygame.K_6:
                game[y][x] = 6
                input_cords[(y, x)] = red
            if event.key == pygame.K_7:
                game[y][x] = 7
                input_cords[(y, x)] = red
            if event.key == pygame.K_8:
                game[y][x] = 8
                input_cords[(y, x)] = red
            if event.key == pygame.K_9:
                game[y][x] = 9
                input_cords[(y, x)] = red
            if event.key == pygame.K_BACKSPACE:
                game[y][x] = None
            if event.key == pygame.K_RETURN:
                input_flag = 0
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                game = [[None for i in range(9)] for j in range(9)]
        if event.type == pygame.KEYDOWN and input_flag == 0:
            if event.key == pygame.K_SPACE:
                input_flag = 1
                sol_flag = 0
                game = [[None for i in range(9)] for j in range(9)]

    if input_flag == 0 and sol_flag == 0:
        solve(0, 0)
        sol_flag = 1

    display_board()
    pygame.display.update()
