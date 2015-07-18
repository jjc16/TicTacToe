'''
@author Joshua Coon
'''

import pygame, sys
from TTTBoard import TTTBoard

SIZE =[400, 300]



pygame.init()

screen=pygame.display.set_mode(SIZE)
board=TTTBoard(screen)
board.draw_blank_board()
board.draw_grid()

chk=True

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        if chk:
            if event.type==pygame.MOUSEBUTTONDOWN:
                r=board.get_hit_rect();
                board.draw_grid()
                
                board.make_move(board.current_player)
                board.write_player_turn()
                chk=board.check_for_win()
    
    pygame.display.flip()