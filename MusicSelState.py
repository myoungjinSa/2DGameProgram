import game_framework
from MusicSelScreen import *
from Sound import *


name ="MusicSelState"

music_Sel = None


def enter():
    global music_Sel
    open_canvas(1160,750)
    music_Sel = MusicSelScreen()
    music_Sel.SetDrawPosX(600,350)
    music_Sel.SetDrawWH(1180,760)




def handle_events():
    global music_Sel
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_d):
            music_Sel.update()


def update():
    global music_Sel




def draw():
    global music_Sel

    clear_canvas()
    music_Sel.draw()

    update_canvas()

def resume():
    pass


def pause():
    pass


def exit():
    close_canvas()


