from pico2d import *
from typing import NamedTuple

CANVAS_WIDTH = 960
CANVAS_HEIGHT = 720
SHEET_HEIGHT = 1024
FRAME_DELAY = 0.08
DISPLAY_HEIGHT = 520
REPEAT_COUNT = 5
PAUSE_SECONDS = 1.0


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

THIRD_FRAMES = (
	Frame(69, 421, 123, 108),
	Frame(249, 429, 90, 100),
	Frame(384, 435, 88, 94),
	Frame(527, 430, 111, 99),
	Frame(665, 439, 99, 90),
	Frame(778, 434, 129, 95),
	Frame(899, 442, 80, 87),
	Frame(1005, 456, 93, 71),
	Frame(1141, 450, 81, 79),
)

FOURTH_FRAMES = (
	Frame(68, 593, 86, 94),
	Frame(237, 598, 74, 89),
	Frame(398, 607, 67, 80),
	Frame(554, 603, 81, 84),
	Frame(731, 602, 73, 86),
	Frame(915, 618, 74, 69),
)

FIFTH_FRAMES = (
	Frame(87, 777, 57, 70),
	Frame(255, 758, 69, 89),
	Frame(433, 727, 62, 105),
	Frame(588, 715, 63, 93),
	Frame(749, 750, 61, 83),
	Frame(903, 775, 60, 72),
)

SIXTH_FRAMES = (
	Frame(59, 909, 64, 81),
	Frame(197, 930, 56, 60),
	Frame(318, 912, 73, 78),
	Frame(452, 916, 59, 74),
	Frame(576, 923, 73, 67),
	Frame(716, 938, 91, 51),
	Frame(854, 938, 90, 51),
	Frame(991, 949, 68, 39),
	Frame(1107, 963, 86, 26),
	Frame(1232, 967, 82, 22),
)

ANIMATIONS = (
	RUN_FRAMES,
	SECOND_FRAMES,
	THIRD_FRAMES,
	FOURTH_FRAMES,
	FIFTH_FRAMES,
	SIXTH_FRAMES,
)


def source_bottom(frame):
	return SHEET_HEIGHT - frame.top - frame.height


def display_size(frame, frames):
	animation_height = max(item.height for item in frames)
	scale = DISPLAY_HEIGHT / animation_height
	return max(1, int(frame.width * scale)), max(1, int(frame.height * scale))


def draw_frame(frame, frames):
	clear_canvas()
	display_width, display_height = display_size(frame, frames)
	sprite_sheet.clip_draw(
		frame.left,
		source_bottom(frame),
		frame.width,
		frame.height,
		CANVAS_WIDTH // 2,
		CANVAS_HEIGHT // 2,
		display_width,
		display_height,
	)
	update_canvas()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sprite_sheet = load_image('animation_sprite_sheet.png')

# The first frame is a measured (x, top, width, height) rectangle.
animation_index = 0
frame_index = 0
completed_plays = 0
running = True

while running:
	for event in get_events():
		if event.type == SDL_QUIT or (
			event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
		):
			running = False
			break
	if not running:
		break

	animation_frames = ANIMATIONS[animation_index]
	frame = animation_frames[frame_index]
	draw_frame(frame, animation_frames)
	delay(FRAME_DELAY)
	frame_index += 1
	if frame_index == len(animation_frames):
		frame_index = 0
		completed_plays += 1
		if completed_plays == REPEAT_COUNT:
			delay(PAUSE_SECONDS)
			completed_plays = 0
			animation_index = (animation_index + 1) % len(ANIMATIONS)
