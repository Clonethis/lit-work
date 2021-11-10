#Ultimate goal: Create makro autoclicker -> that can realtime set-up new makros, also saves current data
# todo 1 -> using 'pyaugui' learn how to get current mouse position 
# todo 2 -> using python library 'time' and for loops, print out mouse position that changes in real time ->
    # bonus point: if mouse is on the same spot don't write anything
# todo 3 -> when mouse touches left border of the screen (x=0) stop program

# docs: https://pyautogui.readthedocs.io/en/latest/mouse.html#mouse-clicks
import pyautogui as pt
# docs: https://docs.python.org/3/library/time.html
import time 
screenSize = pt.size()
print("Screen size: ",screenSize)
previousLocation = pt.position()
for i in range(0,200):
    currentPos = pt.position()
    if previousLocation != currentPos:
        pt.moveTo(screenSize.width/2,screenSize.height/2)
        print("CurrentPos: %d,iterator: %d",currentPos,i)
        previousLocation=currentPos
    time.sleep(0.05)
    if(currentPos.x == 0):
        break
    





# pt.moveTo(screenSize.width/2,screenSize.height/2,0.1)
# pt.alert("nice")
# for i in range(10):
#     pt.click()
#     print('clicking')
#     time.sleep(0.2)