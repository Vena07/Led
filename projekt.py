import machine, time

red = machine.Pin(1, machine.Pin.OUT)
green = machine.Pin(0, machine.Pin.OUT)
blue = machine.Pin(2, machine.Pin.OUT)


button1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button3 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
button4 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

redp = 0
greenp = 0
bluep = 0

red.value(0)
blue.value(0)
green.value(0)

while True:
    if button1.value() == 1 :
        print("button1")
        time.sleep(0.5)
        if redp == 0:
            redp = 1
            red.value(1)
        else:
            redp = 0
            red.value(0)
       
        
    elif button2.value() == 1 :
        print("button2")
        time.sleep(0.5)
        if greenp == 0:
            greenp = 1
            green.value(1)
        else:
            greenp = 0
            green.value(0)
    

    elif button3.value() == 1  :
        print("button3")
        time.sleep(0.5)
        if bluep == 0:
            bluep = 1
            blue.value(1)
        else:
            bluep = 0
            blue.value(0)
    
    elif button4.value() == 1  :
        redp = 0
        greenp = 0
        bluep = 0

        red.value(0)
        blue.value(0)
        green.value(0)