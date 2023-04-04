from gpiozero import Button
from signal import pause

button = Button(26)

# while True:
#     if button.is_pressed: print("Button is pressed !")
#     else: print("Button is not Pressed !")

count = 0

def say_hello():
    global count
    
    count += 1
    print(f"Hello! /cnt : {count}/")
    
def say_bye():
    print("Bye ~")
    
button.when_pressed = say_hello
button.when_released = say_bye
pause()