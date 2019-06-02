import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(22, IO.IN) ## GPIO 14 -> IR sensor as input {}=> orange = 5v, yellow = gnd, green = pin22

while 1:
    if(IO.input(22) == False):
        print("Objeto serca")
        
    else:
        print("NO object")