import random 
import numpy as np
from time import sleep
import sys
import pygame
from pygame.locals import *


# Global Variables for the game
FPS=30
winner=None
draw=False
rows=3
columns=3
width=455
height=600
colour_x=(179,212,252)
white=(255,255,255)
titan_white=(209,221,225)
red=(255,0,0)
dark_blue=(28,116,233)
black=(0,0,0)
# XO='x'
pygame.init()
pygame.display.set_caption('TIC TAC TOE')
screen=pygame.display.set_mode((width,height))

player_x=1
opponent_o=2

## Loading the Images
opening_image=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\tic-tac-toe-python-project\tic-tac-toe-python-project\Enlarged Image.png')
x_img=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\tic-tac-toe-python-project\tic-tac-toe-python-project\X.png')
o_img=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\tic-tac-toe-python-project\tic-tac-toe-python-project\O.png')

## Resizing Images
x_img=pygame.transform.scale(x_img,(80,80))
o_img=pygame.transform.scale(o_img,(80,80))


## TIC_TAC_TOE 3x3 Board
# T=[[None]*3,[None]*3,[None]*3]
board=np.zeros((rows,columns),dtype=int)

game_over=False

def Mark_Square(row,col,player):
    board[row][col]=player

def Available_Square(row,col):
    return board[row][col]==0

def is_board_full():
    for row in range(rows):
        for col in range(columns):
            if board[row][col]==0:
                return False
    return True

def is_moves_left(board):
    for row in range(rows):
        for col in range(columns):
            if board[row][col]==0:
                return True
    return False

def Game_Opening():
    while True:
        ## White Square
        pygame.draw.rect(screen,white,[0,500,455,100])
        ## Opening Image
        screen.blit(opening_image,(0,0))
        Button(30,60,530,'PLAY',89,38)
        Button(30,300,530,'EXIT',89,38)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit
        pygame.display.update()



def Canvas_Board():
    screen.fill(white)
    Rectangle()
    ## Vertical Lines
    pygame.draw.line(screen,black,(150.25,0),(150.25,455),8)
    pygame.draw.line(screen,black,(300.5,0),(300.5,455),8)
    ## Horizontal Lines
    pygame.draw.line(screen,black,(0,150.25),(455,150.25),8)
    pygame.draw.line(screen,black,(0,300.5),(455,300.5),8)

def check_win(player):
    # Vertical win check
    for col in range(columns):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_winning_line(col,player)
            return True
        
    # Horizontal win check
    for row in range(rows):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True
    
    # desc diagonal check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal(player)
        return True
    
    # asc diagonal check
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        draw_asc_diagonal(player)
        return True
    return False


def draw_vertical_winning_line(col,player):
    posx=col*151+75

    pygame.draw.line(screen,red,(posx,25),(posx,height-170),7)
    pygame.display.update()

def draw_horizontal_winning_line(row,player):
    posy=row*151+75

    pygame.draw.line(screen,red,(25,posy),(width-25,posy),7)
    pygame.display.update()

def draw_asc_diagonal(player):
    pygame.draw.line(screen,red,(25,445-25),(width-25,25),7)
    pygame.display.update()

def draw_desc_diagonal(player):
    pygame.draw.line(screen,red,(25,25),(width-25,445-25),7)

def AI_win_status(player):
    if player==1:
        text_wn="AI Won!"
    elif player==2:
        text_wn="X Won!"
    else:
        text_wn="Game Draw"
    font = pygame.font.Font(None, 30)
    text = font.render(text_wn, 1, (0,0,0))
    Rectangle()
    screen.blit(text, (180,500))
    pygame.display.update()

def win_status(player):
    if player==1:
        text_win="X Won!"
    elif player==2:
        text_win="O Won!"
    else:
        text_win="Game Draw"
    font = pygame.font.Font(None, 30)
    text = font.render(text_win, 1, (0,0,0))
    Rectangle()
    screen.blit(text, (180,500))
    pygame.display.update()

def AI_Status(player):
    if player==1:
        text_w="AI's TURN"
    elif player==2:
        text_w="X's TURN"
    font = pygame.font.Font(None, 30)
    text = font.render(text_w, 1, (0,0,0))
    Rectangle()
    screen.blit(text, (180,500))
    pygame.display.update()

def status(player=1):
    if player==1:
        text_win="X's TURN"
    elif player==2:
        text_win="O's TURN"
    font = pygame.font.Font(None, 30)
    text = font.render(text_win, 1, (0,0,0))
    Rectangle()
    screen.blit(text, (180,500))
    pygame.display.update()

def restart():
    for row in range(rows):
        for col in range(columns):
            board[row][col]=0
    print(board)
    Game_Window()
    
def auto_restart():
    sleep(2)
    screen.fill(black)
    Message(30,'RESTARTING GAME',90,245,white,'Yes')
    pygame.display.update()
    sleep(3)
    restart()


def Play_H_VS_H(player):
    global game_over
    Canvas_Board()
    status()
    pygame.display.update()
    while True:
        Button(30,0,height-38,'Restart',width,38)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x=event.pos[0]
                mouse_y=event.pos[1]

                if mouse_y<456:

                    clicked_row=int(mouse_y//151)
                    clicked_col=int(mouse_x//151)

                    if Available_Square(clicked_row,clicked_col):
                        if player==1:
                            status(player)
                            Mark_Square(clicked_row,clicked_col,1)
                            if check_win(player):
                                
                                game_over=False

                            if clicked_row==0 and clicked_col==0:
                                r_clc=clicked_row+30
                                c_clc=clicked_col+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                            elif clicked_row==0 and clicked_col==1:
                                r_clc=151+30
                                c_clc=0+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                            elif clicked_row==0 and clicked_col==2:
                                r_clc=302+30
                                c_clc=0+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()


                                player=2
                                status(player)

                            elif clicked_row==1 and clicked_col==0:
                                r_clc=0+30
                                c_clc=151+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                            elif clicked_row==1 and clicked_col==1:
                                r_clc=151+30
                                c_clc=151+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                            elif clicked_row==1 and clicked_col==2:
                                r_clc=302+30
                                c_clc=151+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                            elif clicked_row==2 and clicked_col==0:
                                r_clc=0+30
                                c_clc=302+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                            elif clicked_row==2 and clicked_col==1:
                                r_clc=151+30
                                c_clc=302+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                            elif clicked_row==2 and clicked_col==2:
                                r_clc=302+30
                                c_clc=302+30

                                screen.blit(x_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=2
                                status(player)

                        elif player==2:
                            status(player)
                            Mark_Square(clicked_row,clicked_col,2)
                            if check_win(player):
                                game_over=False

                            if clicked_row==0 and clicked_col==0:
                                r_clc=0+30
                                c_clc=0+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==0 and clicked_col==1:
                                r_clc=151+30
                                c_clc=0+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==0 and clicked_col==2:
                                r_clc=302+30
                                c_clc=0+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==1 and clicked_col==0:
                                r_clc=0+30
                                c_clc=151+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==1 and clicked_col==1:
                                r_clc=151+30
                                c_clc=151+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==1 and clicked_col==2:
                                r_clc=302+30
                                c_clc=151+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==2 and clicked_col==0:
                                r_clc=0+30
                                c_clc=302+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==2 and clicked_col==1:
                                r_clc=151+30
                                c_clc=302+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)

                            elif clicked_row==2 and clicked_col==2:
                                r_clc=302+30
                                c_clc=302+30

                                screen.blit(o_img,(r_clc,c_clc))
                                pygame.display.update()
                                if check_win(player)==True:
                                    win_status(player)
                                    sleep(1)
                                    auto_restart()
                                elif is_board_full() and check_win(player)==False:
                                    win_status(-1)
                                    sleep(1)
                                    auto_restart()

                                player=1
                                status(player)
                else:
                    pass
def comp_move(player):
    pass

def evaluate(board):

    for row in range(rows):
        if (board[row][0]==board[row][1]) and (board[row][1]==board[row][2]):
            if board[row][0]==1:
                return 10
            elif board[row][0]==2:
                return -10

    for col in range(columns):
        if (board[0][col]==board[1][col]) and (board[1][col]==board[2][col]):
            if board[0][col]==1:
                return 10
            elif board[0][col]==2:
                return -10
    
    if (board[0][0]==board[1][1]) and (board[1][1]==board[2][2]):
        if board[0][0]==1:
            return 10
        elif board[0][0]==2:
            return -10
    if (board[0][2]==board[1][1]) and (board[1][1]==board[2][0]):
        if board[0][2]==1:
            return 10
        elif board[0][2]==2:
            return -10
    
    return 0


def Min_Max(board,depth,isMax):
    score=evaluate(board)

    if score==10:
        return score
    
    if score==-10:
        return score

    if is_moves_left(board)==False:
        return 0
    
    if isMax:
        best=-1000

        for row in range(rows):
            for col in range(columns):
                if board[row][col]==0:
                    board[row][col]=player_x
                    best=max(best,Min_Max(board,depth+1,not isMax))
                    board[row][col]=0
        
        return best
    
    else:
        best=1000

        for row in range(rows):
            for col in range(columns):
                if board[row][col]==0:
                    board[row][col]=opponent_o
                    best=min(best,Min_Max(board,depth+1,not isMax))
                    board[row][col]=0
        
        return best

def Find_Best_Move(board):
    bestVal=-1000
    bestMove=(-1,-1)

    for row in range(rows):
        for col in range(columns):
            if board[row][col]==0:
                board[row][col]=player_x
                moveVal=Min_Max(board,0,False)
                board[row][col]=0

                if moveVal>bestVal:
                    bestMove=(row,col)
                    bestVal=moveVal
    return bestMove


def Play_H_VS_C(player):
    global game_over
    Canvas_Board()
    AI_Status(player)
    pygame.display.update()
    while True:
        Button(30,0,height-38,'Restart',200,38)
        Button(30,214.5,height-38,'EXIT',442,38)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if player==1:
                AI_Status(player)
                pos=Find_Best_Move(board)
                Mark_Square(pos[0],pos[1],1)
                print('\n',board)
                if check_win(player):
                                
                    game_over=False
                if pos[0]==0 and pos[1]==0:
                    r_clc=0+30
                    c_clc=0+30
                    
                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==0 and pos[1]==1:
                    r_clc=151+30
                    c_clc=0+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==0 and pos[1]==2:
                    r_clc=302+30
                    c_clc=0+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==1 and pos[1]==0:
                    r_clc=0+30
                    c_clc=151+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==1 and pos[1]==1:
                    r_clc=151+30
                    c_clc=151+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==1 and pos[1]==2:
                    r_clc=302+30
                    c_clc=151+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==2 and pos[1]==0:
                    r_clc=0+30
                    c_clc=302+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==2 and pos[1]==1:
                    r_clc=151+30
                    c_clc=302+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)

                elif pos[0]==2 and pos[1]==2:
                    r_clc=302+30
                    c_clc=302+30

                    screen.blit(o_img,(r_clc,c_clc))
                    pygame.display.update()
                    if check_win(player)==True:
                        AI_win_status(player)
                        sleep(1)
                        auto_restart()
                    elif is_board_full() and check_win(player)==False:
                        AI_win_status(-1)
                        sleep(1)
                        auto_restart()

                    player=2
                    AI_Status(player)
            
            elif player==2:
                
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_x=event.pos[0]
                    mouse_y=event.pos[1]

                    if mouse_y<456:
                        clicked_row=int(mouse_y//151)
                        clicked_col=int(mouse_x//151)

                        if Available_Square(clicked_row,clicked_col):
                            if player==2:
                                AI_Status(player)
                                Mark_Square(clicked_row,clicked_col,2)
                                if check_win(player):
                                
                                    game_over=False

                                if clicked_row==0 and clicked_col==0:
                                    r_clc=clicked_row+30
                                    c_clc=clicked_col+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)

                                elif clicked_row==0 and clicked_col==1:
                                    r_clc=151+30
                                    c_clc=0+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)

                                elif clicked_row==0 and clicked_col==2:
                                    r_clc=302+30
                                    c_clc=0+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()


                                    player=1
                                    AI_Status(player)

                                elif clicked_row==1 and clicked_col==0:
                                    r_clc=0+30
                                    c_clc=151+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)

                                elif clicked_row==1 and clicked_col==1:
                                    r_clc=151+30
                                    c_clc=151+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)

                                elif clicked_row==1 and clicked_col==2:
                                    r_clc=302+30
                                    c_clc=151+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)

                                elif clicked_row==2 and clicked_col==0:
                                    r_clc=0+30
                                    c_clc=302+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)

                                elif clicked_row==2 and clicked_col==1:
                                    r_clc=151+30
                                    c_clc=302+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)

                                elif clicked_row==2 and clicked_col==2:
                                    r_clc=302+30
                                    c_clc=302+30

                                    screen.blit(x_img,(r_clc,c_clc))
                                    pygame.display.update()
                                    if check_win(player)==True:
                                        AI_win_status(player)
                                        sleep(1)
                                        auto_restart()
                                    elif is_board_full() and check_win(player)==False:
                                        AI_win_status(-1)
                                        sleep(1)
                                        auto_restart()

                                    player=1
                                    AI_Status(player)
                        
                        


def Button(size,x_button,y_button,text,x_set,y_set):                 #Length,Breadth of rectangle
    pygame.draw.rect(screen,colour_x,[x_button,y_button,x_set,y_set])
    Message(size,text,x_button+15,y_button,white)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+x_set and y_button<mouse[1]<y_button+y_set:
        pygame.draw.rect(screen,(0,184,156),[x_button,y_button,x_set,y_set])
        Message(size,text,x_button+15,y_button,white)
        if click==(1,0,0) and text=='PLAY':
            Game_Loop(text)
        elif click==(1,0,0) and text=='Human VS Human':
            Game_Loop(text)
        elif click==(1,0,0) and text=='Human VS Computer':
            Game_Loop(text)
        elif click==(1,0,0) and text=='Restart':
            Game_Loop(text)
        elif click==(1,0,0) and text=='EXIT':
            pygame.quit()
            sys.exit()

def Game_Window():
    screen.fill(white)
    Message(62,'TIC TAC TOE',40,50,dark_blue,'Yes')
    while True:
        Button(30,110,220,'Human VS Human',235,38)
        pygame.display.update()
        Button(30,95,385,'Human VS Computer',265,38)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit
        # pygame.display.update()
    pygame.display.update()

    

def Rectangle():
    ## Creating a rectangle below the canvas.
    pygame.draw.rect(screen,titan_white,[0,458,455,145])
    pygame.display.update()

def Message(size,text,x,y,colour,bold='No'):
    font=pygame.font.SysFont('Arial',size)
    if bold=='Yes':
        font.set_bold(True)
    text=font.render(text,True,colour)
    screen.blit(text,(x,y))

def Game_Loop(text):
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()==(1,0,0) and text=='PLAY':
                    Game_Window()
                    pygame.display.update()
                elif pygame.mouse.get_pressed()==(1,0,0) and text=='Human VS Human':
                    Play_H_VS_H(player=1)
                elif pygame.mouse.get_pressed()==(1,0,0) and text=='Human VS Computer':
                    Play_H_VS_C(player=2)
                elif pygame.mouse.get_pressed()==(1,0,0) and text=='Restart':
                    restart()
        pygame.display.update()

    
if __name__=='__main__':
    Game_Opening()
    # Message(60,'TIC TAC TOE',48,40,(35,102,209),'Yes')
    Game_Loop()