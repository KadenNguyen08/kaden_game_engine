# This file was created by: Kaden Nguyen

'''
health bar
enemy variations
weapons and armor
'''



import pygame as pg
from settings import *
from sprites import *
import sys
from random import randint
from os import path

from math import floor

class Cooldown():
    # sets all properties to zero when instantiated...
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
        # ticking ensures the timer is counting...
    # must use ticking to count up or down
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
    # resets event time to zero - cooldown reset
    def countdown(self, x):
        x = x - self.delta
        if x != None:
            return x
    def event_reset(self):
        self.event_time = floor((pg.time.get_ticks())/1000)
    # sets current time
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        #ticking makes sure that the timer is counting
    #tiking is required to be used to cunt down or up
# Game class is created
def ticking(self):
    self.current_time = floor((pg.time.get_ticks())/1000)
class Game:
    # Methods are created
    def __init__(self):
        pg.init()
        # initialize the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # prints text on the screen
        pg.display.set_caption("My First Video Game")
        # sets the clock
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.running = True
        # game info stored here later on.
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'images')
        self.player_img = pg.image.load(path.join(img_folder, 'Untitled.png')).convert_alpha()
        self.map_data = []   
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                print(self.map_data)
    def new(self):
        self.test_timer = Cooldown()
        print("create new game...")
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        # self.player = Player(self, 10, 10)
        # self.all_sprites.add(self.player)
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            # input
            self.events()
            # processing
            self.update()
            # output
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()
    # methods
    def input(self): 
        pass
    def update(self):
        self.all_sprites.update()
    
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
        pg.display.flip()
     

    def events(self):
            # listening for events
            for event in pg.event.get():
                # hit red x - game closes
                if event.type == pg.QUIT:
                    self.quit()
                    print("the game has ended..")
                # events on the keyboard
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_LEFT:
                #         self.player.move(dx=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_RIGHT:
                #         self.player.move(dx=1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_UP:
                #         self.player.move(dy=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_DOWN:
                #         self.player.move(dy=1)
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

#run the game
g = Game()
# g.show_go_screen()
while True:
    g.new()
    g.run()
    # g.show_go_screen()

