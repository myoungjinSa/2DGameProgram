from pico2d import *
import game_framework
import Board
from NoteManager import *


name = "MainState"


board = None
stage = None
music_time =0.0
note_manager = None
NoteCount =False


def enter():
    global board,note_manager,note_list
    board = Board.Board()
    note_manager = NoteManager()
    note_manager.CreateNoteList(300)
    note_manager.SetElementSelect()




def exit():
    pass


def pause():
   pass





def resume():
   pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key== SDLK_ESCAPE:
            game_framework.quit()



def update():
    global music_time,note_manager,note_list,NoteCount


    if music_time >=0.0:
        note_manager.NoteDown()



    delay(0.01)                             #0.01초 마다
    music_time = music_time + 1

def draw():
    global music_time,board,note_manager

    if music_time %100 == 0  :
        note_manager.SetNotePos()
        note_manager.SetNoteSpeed(3)
        note_manager.UpCurrentIndex()
        note_manager.UpCurrentElementCount()

    local_manager=note_manager.GetNoteList()
    clear_canvas()
    board.draw()
    count = note_manager.GetCurrentIndex()
    for i in range(0,count):
        if local_manager[i].isSelect is True:
            local_manager[i].draw()

    update_canvas()





