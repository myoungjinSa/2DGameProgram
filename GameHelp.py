import game_framework
import MusicSelState
from Board import *
from pico2d import *

helpImage = None
isMusicSel_Start = None

GAME_HELP_POS_X = 580
GAME_HELP_POS_Y = 375

def enter():
    global helpImage,isMusicSel_Start

    helpImage = load_image("Resource\Game_Help.png")
    isMusicSel_Start = False


def exit():
    pass

def handle_events(frame_time):
    global isMusicSel_Start
    events = get_events()
    for event in events:
        if (event.type,event.key) == (SDL_KEYDOWN,SDLK_RETURN):
            if isMusicSel_Start is False:
                isMusicSel_Start = True

        elif event.type == SDL_QUIT:
            game_framework.quit()



def update(frame_time):
    pass


def draw(frame_time):
    global helpImage,isMusicSel_Start


    helpImage.draw(GAME_HELP_POS_X,GAME_HELP_POS_Y)

    update_canvas()

    if isMusicSel_Start is True:
        game_framework.run(MusicSelState)