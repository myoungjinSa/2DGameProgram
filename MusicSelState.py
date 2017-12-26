import game_framework
from MusicSelScreen import *
from Sound import *
import main_state


name ="MusicSelState"

select_screen = None
sample_Music = Sound()
isMain_start = None
key_phamplet = None


def enter():
    global select_screen,isMain_start,key_phamplet

    select_screen = MusicSelScreen()
    index = select_screen.GetCurrentMusic()
    sample_Music.SetMusic(index)
    sample_Music.PlayMusic()
    select_screen.SetDrawPosX(580, 375)
    select_screen.SetDrawWH(1180, 760)

    key_phamplet = load_image("Resource\Key_Phamplet.png")

    isMain_start = False




def handle_events(frame_time):
    global select_screen,sample_Music,isMain_start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_d):
            select_screen.update("right")
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_a):
            select_screen.update("left")
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_RETURN):
            select_screen.SetMusic(select_screen.GetCurrentMusic())
            isMain_start = True


def update(frame_time):
    global select_screen,sample_Music

    if sample_Music.IsChangeMusic(select_screen.GetCurrentMusic()):
        sample_Music.SetMusic(select_screen.GetCurrentMusic())
        sample_Music.PlayMusic()





def draw(frame_time):
    global select_screen,isMain_start,key_phamplet

    clear_canvas()
    select_screen.draw()
    key_phamplet.draw(1000,650,300,200)


    update_canvas()

    if isMain_start is True:
        game_framework.run(main_state)


def resume():
    pass


def pause():
    pass


def exit():
    global select_screen
    del(select_screen)





