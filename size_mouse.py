from time import sleep

from mouse import *


position_big_mouse = []

on_click(lambda: position_big_mouse.append(get_position()))
on_click(lambda: print(position_big_mouse))


try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print('Ctrl+C pressed')
