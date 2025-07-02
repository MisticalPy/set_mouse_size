from time import sleep

import keyboard
from mouse import *
position_big_mouse = [(807, 1055), (21, 917), (124, 574), (762, 326), (1428, 397), (1895, 9)]
position_small_mouse = [(807, 1053), (23, 911), (142, 575), (802, 314), (1341, 398), (1897, 21)]

position_in_this_time = get_position()
position_big_mouse.append(position_in_this_time)
position_small_mouse.append(position_in_this_time)

flag = True


def mouse_set_size(position_big_or_small_mouse):
    for position_x, position_y in position_big_or_small_mouse:
        move(position_x, position_y, absolute=True, duration=0)
        sleep(1.1)
        if position_x != position_big_or_small_mouse[-1][0] and position_y != position_big_or_small_mouse[-1][1]:
            click()


def toggle_mouse_size():
    global flag
    if flag:
        flag = False
        mouse_set_size(position_big_mouse)
    else:
        flag = True
        mouse_set_size(position_small_mouse)


keyboard.add_hotkey("alt", toggle_mouse_size)
try:
    keyboard.wait()
except KeyboardInterrupt:
    print('Interrupted')
