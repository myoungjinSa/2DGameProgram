import game_framework
from pico2d import *
from GameInfoShow import *

from main_state import *
import MusicSelState



name = "GameInfoState"

infoScreen = None

def enter():
    global infoScreen
    infoScreen = GameInfoScreen()

    infoScreen.SetInfoScreenWH(1180,760)
    infoScreen.SetMaxFontPos(200,300)
    infoScreen.SetTotalFontPos(200,500)
    infoScreen.ReadMaxTotalCount()




def resume():
    pass


def exit():
    pass


def pause():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.run(MusicSelState)



def update(frame_time):
    global infoScreen

    infoScreen.update()


def draw(frame_time):
    global infoScreen

    clear_canvas()


    infoScreen.draw()


    update_canvas()
