#Ultimate goal: Create makro autoclicker -> that can realtime set-up new makros, also saves current data
# todo 1 -> using 'pyaugui' learn how to get current mouse position 
# todo 2 -> using python library 'time' and for loops, print out mouse position that changes in real time ->
    # bonus point: if mouse is on the same spot don't write anything
# todo 3 -> when mouse touches left border of the screen (x=0) stop program

# docs: https://pyautogui.readthedocs.io/en/latest/mouse.html#mouse-clicks

# docs: https://docs.python.org/3/library/time.html


import pyautogui as pt 
import time 

a,b = pt.position()
while 1:
    a = pt.position()
    if a != b: 
        b = pt.position()
        print(b)
        time.sleep(0.2)
    elif a.x == 0:
        break