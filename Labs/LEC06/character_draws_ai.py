from pico2d import *
import math
import os

# 실행 위치와 무관하게 이 스크립트가 있는 폴더 기준으로 이미지를 찾음
os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas(800, 600)

character = load_image('character.png')

SPEED = 4


def move_circle():
    print('circle')
    cx, cy, radius = 400, 300, 200
    angle = 0.0
    while angle < 2 * math.pi:
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        angle += 0.01

        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)


def move_along(points):
    x, y = points[0]
    for i in range(1, len(points) + 1):
        gx, gy = points[i % len(points)]
        while True:
            dx = gx - x
            dy = gy - y
            dist = math.sqrt(dx * dx + dy * dy)
            if dist <= SPEED:
                x, y = gx, gy
                break
            x += dx / dist * SPEED
            y += dy / dist * SPEED

            clear_canvas()
            character.draw(x, y)
            update_canvas()
            delay(0.01)


def move_rectangle():
    print('rectangle')
    corners = [(150, 150), (650, 150), (650, 450), (150, 450)]
    move_along(corners)


def move_triangle():
    print('triangle')
    vertices = [(400, 120), (550, 420), (250, 420)]
    move_along(vertices)


while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()