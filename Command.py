import Localdata
from pygame import*
from Basicfunctions import*

def mouse_down(pos):
    if Localdata.enter == False:
        for i in Localdata.buttons:
            if i.rect.collidepoint(pos):
                i.click()
    else:
        if Localdata.local_player._character.alive:
            Localdata.local_player._character.useskill('attack')
            print('attack')
    #clicked a button

def mouse_up(pos):
    pass

def mouse_motion(pos):
     if Localdata.enter:
        if Localdata.local_player._character.alive:
            direction = get_angle(Localdata.local_player._character.pos,pos)*180/pi
            print(direction)
            Localdata.local_player._character.setdirection(direction)

def key_down(key):
    if key == K_w:
        Localdata.local_player._character.movecommand[0] = 1
    if key == K_a:
        Localdata.local_player._character.movecommand[1] = 1
    if key == K_s:
        Localdata.local_player._character.movecommand[2] = 1
    if key == K_d:
        Localdata.local_player._character.movecommand[3] = 1

def key_up(key):
    if key == K_w:
        Localdata.local_player._character.movecommand[0] = 0
    if key == K_a:
        Localdata.local_player._character.movecommand[1] = 0
    if key == K_s:
        Localdata.local_player._character.movecommand[2] = 0
    if key == K_d:
        Localdata.local_player._character.movecommand[3] = 0

def join_game():
    Localdata.local_game.player_join(Localdata.local_player)
    Localdata.local_game.start()
    Localdata.local_player.choose_team('a')
    Localdata.local_player.choose_character('testman')
    Localdata.local_player._character.born()
    Localdata.enter = True