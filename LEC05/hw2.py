from pico2d import *
import math

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

x = 550
y = 300
angle = 0
while True:
    x = 400 + 150 * math.cos(angle)
    y = 300 + 150 * math.sin(angle)
    angle += 0.01


    clear_canvas()
    #grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)
