"""
    Program: CS 115
    Assignment: Project 2
    Author: Maram Salameh
    Description: This program will allow two users to play a variant of
    Tic-Tac-Toe on their choice of board and declare a winner
"""


from graphics import *
import math
import sys


# color player 2 cell choice
def color_red(window, x_clicked, y_clicked, length):
    """
    Purpose: To color a player's 2 choice with red
    Parameters: window: graphing window, x_clicked: clicked x-coordinates
    y_clicked: clicked y-coordinates
    length: size of square
    """
    col = (x_clicked // length)
    row = (y_clicked // length)
    center_x = col * length + (length/2)
    center_y = row * length + (length/2)
    top_left_point = Point(center_x - (length/2),
                           center_y - (length / 2))
    bottom_right_point = Point(center_x + (length/2),
                               center_y + (length / 2))
    rectangle = Rectangle(top_left_point, bottom_right_point)
    rectangle.setFill('red')
    rectangle.draw(window)


# color player 1 cell choice
def color_blue(window, x_clicked, y_clicked, length):
    """
    Purpose: To color a player's 1 choice with blue
    Parameters: window: graphic window, x_clicked: clicked x-coordinates
    y_clicked: clicked y-coordinates
    length: size of square
    """
# find which cell is clicked
    col = (x_clicked // length)
    row = (y_clicked // length)
# find center points and color box
    center_x = col * length + (length/2)
    center_y = row * length + (length/2)
    top_left_point = Point(center_x - (length/2),
                           center_y - (length / 2))
    bottom_right_point = Point(center_x + (length / 2),
                               center_y + (length / 2))
    rectangle = Rectangle(top_left_point, bottom_right_point)
    rectangle.setFill('blue')
    rectangle.draw(window)


# Draw horizontal lines
def draw_horizontal(squares, width, win_size, window):
    """
    Purpose: To draw the horizontal lines of the grid
    Parameters: squares: number of squares per side
    width: square side length, win_size: window size
    window: graphic window
    """
    y1 = width
    first_x = 0
    first_pt = Point(first_x, y1)
    y2 = width
    second_x = win_size
    second_pt = Point(second_x, y2)
    line = Line(first_pt, second_pt)
    line.setOutline('black')
    line.draw(window)
    for j in range(squares - 2):
        y1 += width
        y2 += width
        first_pt = Point(first_x, y1)
        second_pt = Point(second_x, y2)
        line = Line(first_pt, second_pt)
        line.setOutline('black')
        line.draw(window)


def draw_vertical(squares, width, win_size, window):
    """
    Purpose: To draw the vertical lines of the grid
    Parameters: squares: number of squares per side
    width: square side length, win_size: window size
    window: graphic window
    """
    y1 = 0
    first_x = width
    first_pt = Point(first_x, y1)
    y2 = win_size
    second_x = width
    second_pt = Point(second_x, y2)
    line = Line(first_pt, second_pt)
    line.setOutline('black')
    line.draw(window)
    for i in range(squares - 2):
        first_x += width
        second_x += width
        first_pt = Point(first_x, y1)
        second_pt = Point(second_x, y2)
        line = Line(first_pt, second_pt)
        line.setOutline('black')
        line.draw(window)


def is_valid(board, row, col):
    """
    Purpose: To determine whether a player has claimed a cell
    Parameters: board: 2d list of the grid with 0 elements
    row: playes row choice
    col: players column choice
    Returns true if space is available, and False if space is taken
    """
# check if cell is available
    if board[row][col] == 0:
        return True
    else:
        print('Error: Cell is already taken.')
        return False


def check_winner(board, win_squares):
    """
    Purpose: To check which player has won the game
    Parameters: board: 2d list of the grid with 0 elements
    win_squares: the number of required cells in row to win
    Returns winning player
    """
# check for row wins:
    for i in range(len(board)):
        player_1 = 0
        player_2 = 0
        for j in range(len(board)):
            if board[i][j] == '1':
                player_1 += 1
                if player_1 == win_squares:
                    return ('Player 1')
            elif board[i][j] == '2':
                player_2 += 1
                if player_2 == win_squares:
                    return ('Player 2')
            else:
                player_1 = 0
                player_2 = 0

# check for column wins:
    for i in range(len(board)):
            player_1 = 0
            player_2 = 0
            for j in range(len(board)):
                if board[j][i] == '1':
                    player_1 += 1
                    if player_1 == win_squares:
                        return ('Player 1')
                elif board[j][i] == '2':
                    player_2 += 1
                    if player_2 == win_squares:
                        return ('Player 2')
                else:
                    player_1 = 0
                    player_2 = 0

# check for L-R diagonal wins:
    player_1 = 0
    player_2 = 0
    for i in range(len(board)):
        if board[i][i] == '1':
            player_1 += 1
            if player_1 == win_squares:
                return ('Player 1')
        elif board[i][i] == '2':
            player_2 += 1
            if player_2 == win_squares:
                return ('Player 2')
        else:
            player_1 = 0
            player_2 = 0

# check for R-L diagonal wins:
    player_1 = 0
    player_2 = 0
    for i in range(len(board)):
        if board[i][len(board)-(i+1)] == '1':
            player_1 += 1
            if player_1 == win_squares:
                return ('Player 1')
        elif board[i][len(board)-(i+1)] == '2':
            player_2 += 1
            if player_2 == win_squares:
                return('Player 2')
        else:
            player_1 = 0
            player_2 = 0


def main():

    win_size = int(input('Window side length in pixels: '))
    if win_size > 1000 or 100 > win_size:
        print('Error: must be a number between 100 and 1000.')
        sys.exit()
    try:
        squares = int(input('Number of squares per side: '))
        if 3 > squares or squares > math.floor(win_size / 10):
            print('Error: must be a number between 3 and ',
                  math.floor(win_size / 10), '.', sep='')
            sys.exit()
    except ValueError:
        print('Error: must be a number between 3 and ',
                math.floor(win_size / 10), '.', sep='')
        sys.exit()
    win_squares = int(input('Squares in a row to win: '))
    if 1 > win_squares or win_squares > squares:
        print('Error: must be a number between 1 and ', squares, '.', sep='')
        sys.exit()
    window = GraphWin('Tic Tac Toe', win_size, win_size)
    width = (win_size / squares)

    # draw vertiical lines:
    draw_vertical(squares, width, win_size, window)

    # Draw horizontal lines
    draw_horizontal(squares, width, win_size, window)

# Create board
    size = squares
    board = [[0] * size for i in range(size)]

# get mouse clicks and color players' squares --> display winner:
    for i in range(squares ** 2 // 2):
        print('Player 1: click a square.')
        get_c1point = window.getMouse()
        clicked_x = get_c1point.getX()
        clicked_y = get_c1point.getY()
        col = int((clicked_x // width))
        row = int((clicked_y // width))
        if is_valid(board, row, col) is True:
            board[row][col] = '1'
            color_blue(window, clicked_x, clicked_y, width)
            #print(board)
            if check_winner(board, win_squares) == 'Player 1':
                print('Winner: ', check_winner(board, win_squares), '.',
                      ' Click the window to exit.', sep='')
                window.getMouse()
                window.close()
                sys.exit()

        print('Player 2: click a square.')
        get_c2point = window.getMouse()
        clicked2_x = get_c2point.getX()
        clicked2_y = get_c2point.getY()
        col = int((clicked2_x // width))
        row = int((clicked2_y // width))
        if is_valid(board, row, col) is True:
            board[row][col] = '2'
            color_red(window, clicked2_x, clicked2_y, width)
            #print(board)
            if check_winner(board, win_squares) == 'Player 2':
                print('Winner: ', check_winner(board, win_squares), '.',
                      ' Click the window to exit.', sep='')
                window.getMouse()
                window.close()
                sys.exit()

    if squares % 2 == 1:
        print('Player 1: click a square.')
        get_c1point = window.getMouse()
        clicked_x = get_c1point.getX()
        clicked_y = get_c1point.getY()
        col = int((clicked_x // width))
        row = int((clicked_y // width))
        if is_valid(board, row, col) is True:
            board[row][col] = '1'
            color_blue(window, clicked_x, clicked_y, width)
            #print(board)
            if check_winner(board, win_squares) == 'Player 1':
                print('Winner: ', check_winner(board, win_squares), '.',
                      ' Click the window to exit.', sep='')
                window.getMouse()
                window.close()
                sys.exit()


main()
