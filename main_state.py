from pico2d import *
import game_framework
import Board
from NoteManager import *


name = "MainState"


board = None
stage = None
music_time =0.0
note_manager = None


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
    global music_time,note_manager,note_list


    if music_time >0.0:
        note_manager.SetNotePos()
        note_manager.SetNoteSpeed(30)
        note_manager.UpCurrentIndex()
        note_manager.UpCurrentElementCount()
        note_manager.NoteDown()



    delay(0.01)
    music_time = music_time +1.0

def draw():
    global board,note_manager
    count =0
    local_manager=note_manager.GetNoteList()
    clear_canvas()
    board.draw()
    count = note_manager.GetCurrentIndex()
    for i in range(0,count):
        local_manager[i].draw()

    update_canvas()





