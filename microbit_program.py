# Add your Python code here. E.g.
from microbit import *
import random

display.scroll('Mahiro 2020')
display.show(Image.HEART)

while True:
    selection =  random.randint(1, 4)
    
    if selection = 1 :
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)
    elif selection = 2 :
        pin0.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif selection = 3 :
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
    else: # selection = 4
        pin0.write_digital(1)
        pin1.write_digital(1)
        pin2.write_digital(1)
    sleep(500)
