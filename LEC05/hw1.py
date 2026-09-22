from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

x = 200
y = 150
dx = 2
dy = 0
while True:
    x += dx
    y += dy

    if dx == 2 and x >= 600:
        dx = 0
        dy = 2
    if dy == 2 and y >= 450:
        dx = -2
        dy = 0
    if dx == -2 and x <= 200:
        dx = 0
        dy = -2
    if dy == -2 and y <= 150:
        dx = 2
        dy = 0


    clear_canvas()
    #grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

close_canvas()