# Mouse Jiggler v0.1.0 (For Mouse Jiggler W):

from time import sleep
import usb_hid
from adafruit_hid.mouse import Mouse
import board
from digitalio import DigitalInOut, Direction, Pull

size = 250
speed = 1

mouse = Mouse(usb_hid.devices)
statusLED = DigitalInOut(board.LED)
statusLED.direction = Direction.OUTPUT
powerButton = DigitalInOut(board.GP14)
powerButton.direction = Direction.INPUT
powerButton.pull = Pull.UP

power = 0

statusLED.value = False

def checkPowerButton():
    global power
    
    if powerButton.value == 0:
        power = 0

while True:
    if powerButton.value == 0:
        statusLED.value = True
        power = 1
    
    sleep(0.1)

    while power == 1:
        statusLED.value = False
        sleep(0.1)
        statusLED.value = True
        
        for i in range(size):
            checkPowerButton()
            if power == 0:
                break
            
            mouse.move(x=speed)
            sleep(0.01)
            
        if power == 0:
            statusLED.value = False
            sleep(0.2)
            break
            
        statusLED.value = False
        sleep(0.1)
        statusLED.value = True
        
        for i in range(size):
            checkPowerButton()
            if power == 0:
                break
            
            mouse.move(y=-speed)
            sleep(0.01)
            
        if power == 0:
            statusLED.value = False
            sleep(0.2)
            break
            
        statusLED.value = False
        sleep(0.1)
        statusLED.value = True
            
        for i in range(size):
            checkPowerButton()
            if power == 0:
                break
            
            mouse.move(x=-speed)
            sleep(0.01)
            
        if power == 0:
            statusLED.value = False
            sleep(0.2)
            break
            
        statusLED.value = False
        sleep(0.1)
        statusLED.value = True
            
        for i in range(size):
            checkPowerButton()
            if power == 0:
                break
            
            mouse.move(y=speed)
            sleep(0.01)
        
        if power == 0:
            statusLED.value = False
            sleep(0.2)
            break
