#Ultimate goal: Create makro autoclicker -> that can realtime set-up new makros, also saves current data
# todo 1 -> using 'pyaugui' learn how to get current mouse position 
# todo 2 -> using python library 'time' and for loops, print out mouse position that changes in real time ->
    # bonus point: if mouse is on the same spot don't write anything
# todo 3 -> when mouse touches left border of the screen (x=0) stop program

# docs: https://pyautogui.readthedocs.io/en/latest/mouse.html#mouse-clicks
import pyautogui as pt
# docs: https://docs.python.org/3/library/time.html
import time 

"""
a,b = pt.position()
def(mouse_moves(a,b)):
    for a != b:

if mouse 
    for  
        print(pt.position())
else nic 

"""
now,previous = pt.position()
print(type(now.x))
print('pt.size:',pt.size())
while 1:
    if now.x == 0:
        break
    time.sleep(0.2)
    now = pt.position()
    if now != previous:
        previous = now  
        print(now)
    else:
        print('',end = '')