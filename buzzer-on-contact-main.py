# Imports go at the top
from microbit import *

while True:
    if pin0.read_analog() > 500:
        display.show(Image.HEART)
    else:
        display.show(Image.ANGRY)
    sleep(100)