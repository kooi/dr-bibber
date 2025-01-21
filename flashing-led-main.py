# Imports go at the top
from microbit import *

#pin2 # red
#pin1 # green

teller = 0

while True:
    teller = teller +1
    if teller %2 == 0:
        pin2.write_digital(1)
        pin1.write_digital(0)
    else:
        pin1.write_digital(1)
        pin2.write_digital(0)
    sleep(100)