from time import sleep

from mouse import *

position_big_mouse = [(805, 1053), (21, 918), (175, 574), (784, 323), (1428, 398)]

for position_x, position_y in position_big_mouse:
    move(position_x, position_y, absolute=True, duration=0)
    sleep(0.3)
    click()
