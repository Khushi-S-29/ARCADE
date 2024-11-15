import pygame
import sys
import random
import time

pygame.init()

BACKGROUND_COLOR = (191, 172, 200)
LINE_COLOR = (39, 48, 67)  # Dark Blue color for lines
LINE_WIDTH = 15
CIRCLE_COLOR = (28, 170, 156)  # Teal color for O's
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_COLOR = (242, 85, 96)  # Soft Red color for X's
CROSS_WIDTH = 25
GAME_OVER_COLOR = MY_COLOR = (79, 18, 113)
TEXT_COLOR = (0, 0, 0)  # Dark color for result messages
FONT = pygame.font.SysFont("Arial", 48)
SMALL_FONT = pygame.font.SysFont("Arial", 24)

board = [['-' for _ in range(3)] for _ in range(3)]
current_player = 'X'  # Player starts
game_over_message = ''
game_result_color = GAME_OVER_COLOR

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    for row in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, row * height // 3), (width, row * height // 3), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * width // 3, 0), (row * width // 3, height), LINE_WIDTH)

def draw_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * width // 3 + 50, row * height // 3 + 50),
                                 (col * width // 3 + width // 3 - 50, row * height // 3 + height // 3 - 50), 
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * width // 3 + width // 3 - 50, row * height // 3 + 50),
                                 (col * width // 3 + 50, row * height // 3 + height // 3 - 50), 
                                 CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * width // 3 + width // 6, row * height // 3 + height // 6), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            screen.fill((255, 182, 193))
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':
            screen.fill((255, 182, 193))
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != '-':
        screen.fill((255, 182, 193))
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        screen.fill((255, 182, 193))
        return board[0][2]
    
    
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                moves.append((i, j))
    return moves

def minimax(board, depth, alpha, beta, maximizing_player):
    score = evaluate(board)

    if score == 10 or score == -10 or is_board_full(board):
        return score

    if maximizing_player:
        max_eval = -float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'  # AI's move
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move[0]][move[1]] = '-'  # Undo move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'  # Player's move
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move[0]][move[1]] = '-'  # Undo move
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def evaluate(board):
    if check_winner(board) == 'O':
        return 10  # AI wins
    
    elif check_winner(board) == 'X':
        return -10  
    
    return 0  

def opponent_move():
    best_move = None
    best_value = -float('inf')
    
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'  # Make the AI move
        move_value = minimax(board, 0, -float('inf'), float('inf'), False)
        board[move[0]][move[1]] = '-'  # Undo move
        
        if move_value > best_value:
            best_value = move_value
            best_move = move
    
    board[best_move[0]][best_move[1]] = 'O'

def draw_buttons():
    restart_button = pygame.Rect(width // 3 + 25, height // 3 + 100, 150, 50)
    pygame.draw.rect(screen, (0, 255, 0), restart_button)
    restart_text = SMALL_FONT.render("Restart", True, TEXT_COLOR)
    screen.blit(restart_text, (restart_button.x + 45, restart_button.y + 10))

    quit_button = pygame.Rect(width // 3 + 25, height // 3 + 160, 150, 50)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    quit_text = SMALL_FONT.render("Quit", True, TEXT_COLOR)
    screen.blit(quit_text, (quit_button.x + 55, quit_button.y + 10))

    return restart_button, quit_button


def play_tic_tac_toe():
    global current_player, game_over_message, game_result_color
    running = True
    game_over_message = ""
    
    while running:
        if game_over_message:
            screen.fill((255, 182, 193))  
        else:
            screen.fill(BACKGROUND_COLOR)  

        draw_grid()
        draw_marks()

        if game_over_message:
            screen.fill((255, 182, 193))
            message = FONT.render(game_over_message, True, TEXT_COLOR)
            screen.blit(message, (width // 3, height // 3))
            restart_button, quit_button = draw_buttons()
            pygame.display.update()
            handle_buttons(restart_button, quit_button)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over_message:
                if current_player == 'X':
                    x, y = event.pos
                    row, col = y // (height // 3), x // (width // 3)
                    if board[row][col] == '-':
                        board[row][col] = 'X'

                        winner = check_winner(board)
                        if winner:
                            game_over_message = f"Player {winner} Wins!"
                            game_result_color = CROSS_COLOR if winner == 'X' else CIRCLE_COLOR
                        elif is_board_full(board):
                            game_over_message = "It's a Tie!"
                            game_result_color = LINE_COLOR  
                        else:
                            current_player = 'O'
                            draw_grid()
                            draw_marks()
                            pygame.display.update()

                            time.sleep(0.5)  
                            opponent_move()
                            winner = check_winner(board)
                            if winner:
                                game_over_message = f"COMPUTER WINS!"
                                game_result_color = CIRCLE_COLOR
                            elif is_board_full(board):
                                game_over_message = "It's a Tie!"
                                game_result_color = LINE_COLOR  # Color for tie message
                            else:
                                current_player = 'X'

    pygame.quit()
    sys.exit()

def handle_buttons(restart_button, quit_button):
    global board, current_player, game_over_message, game_result_color
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if restart_button.collidepoint(x, y):
                    board = [['-' for _ in range(3)] for _ in range(3)]
                    current_player = 'X'
                    game_over_message = ''
                    play_tic_tac_toe()
                    return
                elif quit_button.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

play_tic_tac_toe()