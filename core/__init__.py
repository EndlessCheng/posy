import sys

import pygame
from pygame.locals import *

from utils import get_res_file_path

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
OS_NAME = "Posy"

COLOR_WIN98_DESKTOP = (0, 132, 132)
COLOR_BLACK = (0, 0, 0)
COLOR_DARK = (132, 132, 132)
COLOR_GRAY = (198, 198, 198)
COLOR_WHITE = (255, 255, 255)

TIMER = pygame.time.Clock()
DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def init_desktop():
    DISPLAY_SURF.fill(COLOR_WIN98_DESKTOP)
    pygame.draw.rect(DISPLAY_SURF, COLOR_GRAY, (0, SCREEN_HEIGHT - 28, SCREEN_WIDTH, 28))
    pygame.draw.rect(DISPLAY_SURF, COLOR_WHITE, (0, SCREEN_HEIGHT - 27, SCREEN_WIDTH, 1))

    pygame.draw.rect(DISPLAY_SURF, COLOR_WHITE, (3, SCREEN_HEIGHT - 24, 57, 1))
    pygame.draw.rect(DISPLAY_SURF, COLOR_WHITE, (2, SCREEN_HEIGHT - 24, 1, 21))
    pygame.draw.rect(DISPLAY_SURF, COLOR_DARK, (3, SCREEN_HEIGHT - 4, 57, 1))
    pygame.draw.rect(DISPLAY_SURF, COLOR_DARK, (59, SCREEN_HEIGHT - 23, 1, 19))
    pygame.draw.rect(DISPLAY_SURF, COLOR_BLACK, (2, SCREEN_HEIGHT - 3, 58, 1))
    pygame.draw.rect(DISPLAY_SURF, COLOR_BLACK, (60, SCREEN_HEIGHT - 24, 1, 22))

    pygame.draw.rect(DISPLAY_SURF, COLOR_DARK, (SCREEN_WIDTH - 47, SCREEN_HEIGHT - 24, 41, 1))
    pygame.draw.rect(DISPLAY_SURF, COLOR_DARK, (SCREEN_WIDTH - 47, SCREEN_HEIGHT - 23, 1, 20))
    pygame.draw.rect(DISPLAY_SURF, COLOR_WHITE, (SCREEN_WIDTH - 47, SCREEN_HEIGHT - 3, 44, 1))
    pygame.draw.rect(DISPLAY_SURF, COLOR_WHITE, (SCREEN_WIDTH - 3, SCREEN_HEIGHT - 24, 1, 22))

    font_obj = pygame.font.Font('freesansbold.ttf', 16)
    text_surface_obj = font_obj.render('Start', True, COLOR_BLACK)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (32, SCREEN_HEIGHT - 12)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)

    font_obj = pygame.font.Font('freesansbold.ttf', 11)
    text_surface_obj = font_obj.render('12: 00', True, COLOR_BLACK)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (SCREEN_WIDTH - 24, SCREEN_HEIGHT - 12)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)

    pygame.display.update()


def play_start_sound():
    start_sound = pygame.mixer.Sound(get_res_file_path('start.wav'))
    start_sound.play()


def play_shutdown_animation():
    DISPLAY_SURF.fill(COLOR_BLACK)

    frame = 8
    step = SCREEN_WIDTH / (2 * frame)
    for i in range(frame + 1):
        h = i // 4 + 1
        pygame.draw.rect(DISPLAY_SURF, COLOR_BLACK,
                         (0, (SCREEN_HEIGHT - h) // 2, SCREEN_WIDTH, h))
        pygame.draw.rect(DISPLAY_SURF, COLOR_WHITE,
                         (step * i, (SCREEN_HEIGHT - h) // 2, SCREEN_WIDTH - 2 * step * i, h))
        pygame.display.update()
        TIMER.tick(60)


def shutdown():
    play_shutdown_animation()

    pygame.quit()
    sys.exit()


def handle_event(event):
    etype = event.type
    if etype == QUIT:
        shutdown()


def main():
    pygame.display.set_caption(OS_NAME)

    init_desktop()
    play_start_sound()

    while True:
        for event in pygame.event.get():
            handle_event(event)  # 处理相关中断

        pygame.display.update()


if __name__ == '__main__':
    main()
