from Sound import *
from gameManager import *
from pico2d import *

import game_framework

name = "Custom"


music = SOUND()
file =None
Current_Time =0.0
music_interval =0.0

def enter():
    global music,file
    open_canvas()
    music.SetMusic("Shape_of_you.mp3")
    music.PlayMusic()

    file = open("ddd.txt","w")


def handle_events():
    global Current_Time,music_interval
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
            music_interval = get_time() -Current_Time
            file.write(str(music_interval))
            file.write("\n")

def exit():
    close_canvas()
    file.close()

def pause():
    pass

def resume():
    pass


def update():
    global Current_Time
    Current_Time = get_time()



def draw():
    pass
