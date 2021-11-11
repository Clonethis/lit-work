
# TODO 1 - create function/code 
#that on keypress letter 'm' will add current position into list'mousePositions' and 'd' will remove last element(in if user adds wrong data), on key 'x' exit ;
#pop function for removing last element: https://www.geeksforgeeks.org/python-list-pop/
#append fc for adding element : https://www.w3schools.com/python/ref_list_append.asp
# you can create code using switch match, which would be more suitable for this position -> syntax of match : https://www.tabnine.com/blog/the-essential-guide-to-python-switch-statements/
# user input: https://www.w3schools.com/python/python_user_input.asp
#key strokes : https://pyautogui.readthedocs.io/en/latest/keyboard.html
# TODO 2 - print saved 'mousePositions' into output libraries'data.txt' using python;
# another tutorial for inputing txt into file: https://www.geeksforgeeks.org/file-handling-python/ 
# inputing into txt: https://www.geeksforgeeks.org/python-copy-contents-of-one-file-to-another-file/
# TODO 3 - on start of program let user decide if he wants to load saved data or create new routine;

# -> also provide error if user creates something wrong
#cmd:  'Would you like to 'create' new or 'load' old data? Press 'c' or 'l''
import pyautogui as pt

userDecider = input("Would you like to 'create' new or 'load' old data? Press 'c' or 'l'")
if userDecider == 'c':
    demo_file = open('values.txt','w')
elif userDecider == 'l':
    demo_file = open('values.txt','a')

mousePositions = []
for i in range(20):
    list_operator = input("neco napus pyco ")
    if list_operator == 'm':
        mousePositions.append(pt.position())
        print(pt.position(), 'was added to the list')
        print("actual list", mousePositions)
        #pt.sleep(1)
    elif list_operator == 'd':
        mousePositions.pop()
        print('the last element of the list was removed')
        print("new list", mousePositions)
    elif list_operator == 'x':
        demo_file.write(str(mousePositions))
        demo_file.close()
        print('data is now stored in values.txt; ending program')
        break
    else:
        print('ne')
        

