import game_framework
from MusicSelScreen import *
from Sound import *
import main_state


name ="MusicSelState"

music_Sel = None
Sample_Music = Sound()

def enter():
    global music_Sel

    music_Sel = MusicSelScreen()
    index = music_Sel.GetCurrentMusic()
    Sample_Music.SetMusic(index)
    Sample_Music.PlayMusic()
    music_Sel.SetDrawPosX(580,375)
    music_Sel.SetDrawWH(1180,760)




def handle_events(frame_time):
    global music_Sel,Sample_Music
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_d):
            music_Sel.update("right")
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_a):
            music_Sel.update("left")
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_RETURN):
            saveMusic = open("Text\SelMusic.txt","w")
            saveMusic.write(str(music_Sel.GetCurrentMusic()))
            saveMusic.close()
            game_framework.run(main_state)


def update(frame_time):
    global music_Sel,Sample_Music

    if Sample_Music.IsChangeMusic(music_Sel.GetCurrentMusic()):
        Sample_Music.SetMusic(music_Sel.GetCurrentMusic())
        Sample_Music.PlayMusic()





def draw(frame_time):
    global music_Sel

    clear_canvas()
    music_Sel.draw()

    update_canvas()

def resume():
    pass


def pause():
    pass


def exit():
    global music_Sel
    del(music_Sel)


