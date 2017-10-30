import game_framework
from pico2d import *
import main_state



name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1180,750)
    image = [load_image('Board.bmp'),load_image("stage_bitmap.bmp")]



def exit():
    global image
    del (image)

    close_canvas()



def update():
    global logo_time

    if(logo_time>1.0):
        logo_time = 0
       # game_framework.quit()
        game_framework.push_state(main_state)

    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    image[0].draw(300,350)
    image[1].draw(890,350)
    update_canvas()





def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




