from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
frame = 0

while True:
    start = 800
    end = 0
    step = -5
    for bottom in range(0,301,100):
        for x in range(start, end, step):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(
                frame * 100, bottom, # left, bottom
                100, 100,       # width, height
                x, 90,          # x, y
                200, 200
            )
            update_canvas()

            frame = (frame + 1) % 8
            delay(0.05)
        start, end = end, start
        step *= -1




close_canvas()

