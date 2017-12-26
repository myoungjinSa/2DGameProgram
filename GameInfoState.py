import game_framework
from pico2d import *
from GameInfoShow import *

import main_state
import MusicSelState



name = "GameInfoState"

infoScreen = None
max_hit = None
total_hit = None
isMusicSel= None

def enter():
    global infoScreen,max_total,total_hit,isMusicSel

    max_total = main_state.max_total
    total_hit = main_state.total_hit
    infoScreen = GameInfoScreen()

    infoScreen.SetInfoScreenWH(1180,760)
    infoScreen.SetMaxFontPos(200,300)
    infoScreen.SetTotalFontPos(200,500)
    infoScreen.ReadMaxTotalCount(max_total,total_hit)

    isMusicSel = False


def resume():
    pass


def exit():
    pass


def pause():
    pass

def handle_events(frame_time):
    global isMusicSel
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            if isMusicSel == False:
                isMusicSel = True



def update(frame_time):
    global infoScreen

    infoScreen.update()



def draw(frame_time):
    global infoScreen,isMusicSel

    clear_canvas()


    infoScreen.draw()


    update_canvas()


    if isMusicSel is True:
        game_framework.run(MusicSelState)