
# TODO 1 - create function/code that on keypress letter 'm' will add current position into list'mousePositions' and 'd' will remove last element(in case user adds wrong data), on key 'x' exit ;
#pop function for removing last element: https://www.geeksforgeeks.org/python-list-pop/
#append fc for adding element : https://www.w3schools.com/python/ref_list_append.asp
# you can create code using switch match, which would be more souitable for this position -> syntax of match : https://www.tabnine.com/blog/the-essential-guide-to-python-switch-statements/
# user input: https://www.w3schools.com/python/python_user_input.asp
#key strokes : https://pyautogui.readthedocs.io/en/latest/keyboard.html
# TODO 2 - print saved 'mousePositions' into using python output libraries'data.txt';
# another tutorial for inputing txt into file: https://www.geeksforgeeks.org/file-handling-python/ 
# inputing into txt: https://www.geeksforgeeks.org/python-copy-contents-of-one-file-to-another-file/
# TODO 3 - on start of program let user decide if he wants to load saved data or create new routine;

# -> also provide error if user creates something wrong
#cmd:  'Would you like to 'create' new or 'load' old data? Press 'c' or 'l''
import pyautogui as pt
userDecider = input("Would you like to 'create' new or 'load' old data? Press 'c' or 'l'")