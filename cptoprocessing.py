import board #pylint: disable-msg=import-error
import time
import simpleio #pylint: disable-msg=import-error
import busio #pylint: disable-msg=import-error
from analogio import AnalogIn #pylint: disable-msg=import-error
potPin = AnalogIn(board.A2)
potentiometer = 0
arr = 0

uart = busio.UART(board.TX, board.RX, baudrate=9600) #pylint: disable-msg=import-error

while True:

    myPotValue = potPin.value
    potentiometer = int(simpleio.map_range(myPotValue, 0, 65535, 0, 255))
    arr = bytes([potentiometer])
    uart.write(arr)
    print((arr))
    time.sleep(.11)
