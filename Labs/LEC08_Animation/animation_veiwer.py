from pico2d import *
from typing import NamedTuple

CANVAS_WIDTH = 960
CANVAS_HEIGHT = 720
SHEET_HEIGHT = 1024
FRAME_DELAY = 0.08
DISPLAY_HEIGHT = 520


class Frame(NamedTuple):
	left: int
	top: int
	width: int
	height: int


RUN_FRAMES = (
	Frame(73, 50, 70, 119),
	Frame(245, 70, 58, 99),
	Frame(398, 75, 49, 94),
	Frame(540, 70, 51, 99),
	Frame(681, 59, 57, 110),
	Frame(825, 72, 54, 97),
	Frame(961, 83, 45, 86),
	Frame(1081, 85, 43, 84),
)

SECOND_FRAMES = (
	Frame(67, 234, 69, 118),
	Frame(201, 247, 58, 105),
	Frame(322, 254, 56, 98),
	Frame(435, 255, 60, 97),
	Frame(547, 256, 59, 96),
	Frame(658, 256, 58, 96),
	Frame(767, 255, 55, 97),
	Frame(877, 250, 65, 102),
	Frame(998, 241, 66, 111),
	Frame(1119, 250, 58, 102),
	Frame(1228, 255, 51, 97),
	Frame(1328, 263, 48, 89),
	Frame(1427, 265, 50, 87),
)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sprite_sheet = load_image('animation_sprite_sheet.png')

# The first frame is a measured (x, top, width, height) rectangle.
frame = RUN_FRAMES[0]

while True:
	clear_canvas()
	left, top, width, height = frame
	scale = DISPLAY_HEIGHT / height
	sprite_sheet.clip_draw(
		left,
		SHEET_HEIGHT - top - height,
		width,
		height,
		CANVAS_WIDTH // 2,
		CANVAS_HEIGHT // 2,
		int(width * scale),
		DISPLAY_HEIGHT,
	)
	update_canvas()
	delay(FRAME_DELAY)
