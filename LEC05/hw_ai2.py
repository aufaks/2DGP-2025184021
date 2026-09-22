from pico2d import *
import math


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

# 원운동의 기준: 화면 중앙을 중심으로, 화면 안에 들어오는 반지름
CENTER_X, CENTER_Y = 400, 300
RADIUS = 200

angle = 0.0   # 현재 각도 (라디안)

while True:
    # 각도에 해당하는 x, y 좌표 계산
    x = CENTER_X + RADIUS * math.cos(angle)
    y = CENTER_Y + RADIUS * math.sin(angle)

    # 각도를 조금씩 증가시키며 계속 순환 → 끊기지 않는 반복 운동
    angle += 0.02

    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

close_canvas()