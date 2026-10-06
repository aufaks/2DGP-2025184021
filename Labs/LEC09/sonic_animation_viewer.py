import pico2d

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        pass
    finally:
        pico2d.close_canvas()


if __name__ == "__main__":
    main()