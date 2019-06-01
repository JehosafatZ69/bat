import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(22, IO.IN) ## GPIO 14 -> IR sensor as input

while 1:
    if(IO.input(22) == False):
        print("Objeto serca")
        
    else:
        print("NO object")