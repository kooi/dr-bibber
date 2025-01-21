# Imports go at the top
from microbit import *

while True:
    if pin0.read_analog() > 500:
        display.show(Image.HEART)
        pin2.write_digital(1)
        pin1.write_digital(0)
    else:
        display.show(Image.ANGRY)
        pin1.write_digital(1)
        pin2.write_digital(0)

    sleep(100)