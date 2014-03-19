#Finch Celebration Program
#authors: Simon, Juhi, Andrew

from finch import *
from time import sleep, time

finch = Finch()

finch.wheels(-1,1)
sleep(3)
finch.wheels(1,-1)
sleep(3)
finch.wheels(0,0)

#Taken from alarm.py
x = 0
while x > -0.5:
    x, y, z, tap, shake = finch.acceleration()
    #The finch plays the Jaws theme song while changing its lights from red to blue continuously 
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 329) # first note in the jaws theme song
    sleep(1.05)
    finch.led("#0000FF") # set the led to blue
    finch.buzzer(1.0, 349)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 329)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 349)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 311)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 293)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 277)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 277)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 293)
    sleep(1.05)
    finch.led("#FF0000") # set the led to red
    finch.buzzer(1.0, 311)
    sleep(1.05)

finch.wheels(-1,1)
sleep(3)
finch.wheels(1,-1)
sleep(3)
finch.wheels(0,0)

finch.halt()
finch.close()
