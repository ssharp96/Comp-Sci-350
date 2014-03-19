#Finch Maze Program
#authors: Simon, Juhi, Andrew

from finch import Finch
from time import sleep, time

finch = Finch()

finch.led(255, 0, 0) # Turns light red

start = time()

#Makes Finch drive through track and then celebrate at the end
finch.wheels(.8, .87) 
sleep(5.5)
finch.wheels(0, 1)
sleep(.6)
finch.led(225, 0, 225)
finch.wheels(.8, .83)
sleep(2.5)
finch.wheels(1, 0)
sleep(.35)
finch.led(0, 150, 150)
finch.wheels(.8, .81)
sleep(8)
finch.wheels(0, 0)
finch.wheels(-1,1)
sleep(3)
finch.wheels(1, -1)
sleep(3)
finch.wheels(0,0)
