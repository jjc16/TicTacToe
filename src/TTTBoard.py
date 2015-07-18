'''
Created on Jul 12, 2015

@author: Joshua
'''
#from Main import screen
import pygame
from math import floor
from Player import Player 

WHITE = (255,255,255)
BLACK = (0,0,0)

LINES=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6),]

class TTTBoard(object):
    '''
    classdocs
    '''
    
    def __init__(self, screen):
        '''
        Constructor
        '''
        self.screen=screen
        self.rect_array=[];
        self.turn_rect=[];
        
        self.player_X=Player('X')
        self.player_O=Player('O')
        self.current_player=self.player_X;
        
        self.filled_squares={};
        self.text=[];
        self.textpos=[];      
        
        
    def draw_blank_board(self):
        #create a blank tic-tac-toe board
        
        self.screen.fill(WHITE)  
        
        height=self.screen.get_height();
        width=self.screen.get_width();
        
        x=[0,1, 2]
        z=[[ii,jj] for ii in x for jj in x]; #hooray list comprehension!
        
        for zz in z:
            self.rect_array.append(pygame.draw.rect(self.screen,WHITE,[floor(zz[0]*width/4),floor(zz[1]*height/4),floor(width/4),floor(height/4)],0))
            #print(self.rect_array)
        #self.turn_rect=pygame.draw.rect(self.screen,(255,255,0),[floor(width-width/8),floor(height/8),floor(width/9),floor(height/9)],0)
        self.initialize_filled_squares()
    
    def initialize_filled_squares(self):
        for rect in self.rect_array:
            self.filled_squares[rect.center]=[];
    
    def make_move(self,player):
        
        rect=self.get_hit_rect();
        #cntr=rect.center();
        draw_bool=self.check_if_rect_empty(rect)        
        self.set_move_history(rect, player)
        
        if not draw_bool:
            if player.mark=='X':
                self.draw_X(rect)
            elif player.mark=='O':
                self.draw_O(rect)
                
            self.change_current_player(rect)
            self.del_player_turn_text()
        else:
            pass

    
    def draw_X(self,rect):
        
        if rect !=None:
            pygame.draw.line(self.screen,BLACK,rect.topright,rect.bottomleft,3)
            pygame.draw.line(self.screen,BLACK,rect.topleft,rect.bottomright,3)
        
    def draw_O(self,rect):
        
        if rect !=None:
            pygame.draw.ellipse(self.screen,BLACK,rect,3)
        
    
    def draw_grid(self):
        
        height=self.screen.get_height();
        width=self.screen.get_width();
        
        pygame.draw.line(self.screen,BLACK,[floor(width/4),0], [floor(width/4),height-height/4],5) 
        pygame.draw.line(self.screen,BLACK,[floor(2*width/4),0], [floor(2*width/4),height-height/4],5)
        pygame.draw.line(self.screen,BLACK,[0,floor(2*height/4)], [width-width/4,floor(2*height/4)],5)  
        pygame.draw.line(self.screen,BLACK,[0,floor(height/4)], [width-width/4,floor(height/4)],5)
       
    def get_hit_rect(self):
        
        pos=pygame.mouse.get_pos();
        #r=[];
        print(pos[0],pos[1])
        
        for rect in self.rect_array:
            if pos[0] > rect.left and  pos[0] < rect.right and pos[1] > rect.top and pos[1] < rect.bottom:
                #print(rect)
                #pygame.draw.rect(self.screen,(0,255,0),rect,0)
                return rect;
            
    def set_move_history(self,rect,player):
        
        if rect != None:
            self.filled_squares[rect.center]=player.mark;
                
    def check_if_rect_empty(self,rect):
        
        if rect!=None:
            chk=self.filled_squares[rect.center]
        else:
            chk= False
            return
        
        if chk:
            return True
        else:
            return False

    def change_current_player(self,rect):
        
        if rect != None:
            if self.current_player==self.player_X:
                self.current_player=self.player_O
            elif self.current_player==self.player_O:
                self.current_player=self.player_X

    def check_for_win(self):

        for line in LINES:
            r1=[];
            for x in line:
                r1.append(self.filled_squares[tuple(self.rect_array[x].center)])
            #print(r1)   
            if all(r=='X' for r in r1):
                message='X wins!'
                self.print_winning_meesage(message)
                return False
            elif all(r=='O' for r in r1):
                message='O wins'
                self.print_winning_meesage(message)
                return False
        return True
       
    def print_winning_meesage(self,message):
        textpos=[floor(3*self.screen.get_width()/4),floor(self.screen.get_height()-self.screen.get_height()/8)]
        font=pygame.font.Font(None,36)
        text=font.render(message,0,(0,0,0))
        self.screen.blit(text,textpos)
        pygame.display.flip()
              
    def write_player_turn(self):
        
        font=pygame.font.Font(None,36)
        self.textpos=[floor(self.screen.get_width()/16),floor(self.screen.get_height()-self.screen.get_height()/8)]

        player_turn='Player turn: ' + self.current_player.mark;
        self.text=font.render(player_turn,0,(0,0,0))
        self.screen.blit(self.text,self.textpos)
        pygame.display.flip()
        
    def del_player_turn_text(self):
            if self.text:
                rect_size=self.text.get_rect();
                #print(rect_size)
                #print(self.textpos)
                pygame.draw.rect(self.screen,(255,255,255),[self.textpos[0],self.textpos[1], rect_size[2],rect_size[3]],0)
                pygame.display.flip()
            