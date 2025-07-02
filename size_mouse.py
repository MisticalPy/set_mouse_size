from time import sleep

import keyboard
from mouse import *

position_big_mouse = [(832, 1055), (22, 917), (135, 574), (762, 326), (1428, 397), (1895, 9)]
position_small_mouse = [(832, 1053), (23, 911), (142, 575), (802, 314), (1341, 398), (1897, 21)]

position_in_this_time = get_position()
position_big_mouse.append(position_in_this_time)
position_small_mouse.append(position_in_this_time)

flag = True


def mouse_set_size(position_big_or_small_mouse):
    for position_x, position_y in position_big_or_small_mouse:
        move(position_x, position_y, absolute=True, duration=0)
        sleep(1.2)
        if position_x != position_big_or_small_mouse[-1][0] and position_y != position_big_or_small_mouse[-1][1]:
            click()


try:
    while True:
        sleep(1)
        if keyboard.is_pressed('alt'):
            sleep(0.5)
            if flag:
                flag = False
                mouse_set_size(position_big_mouse)
            else:
                flag = True
                mouse_set_size(position_small_mouse)
except KeyboardInterrupt:
    print('end')
