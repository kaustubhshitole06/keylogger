#hellofrom pynput.mouse import Controller
from pynput.keyboard import Controller

#def mousecontrol():
    #mouse = Controller()
    #mouse.position = (20, 30)
   
#mousecontrol()

def keyboardcontrol():
    keyboard = Controller()
    keyboard.type("hello")

keyboardcontrol() #hellohello