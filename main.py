# notify
import utime as time

from gates import GateIn
from leds import LED

print('RUN: main.py')

from machine import Pin, SPI

class MCP4822:
    """
    """
    GAIN_BYTE = 13
    CHANNEL_SELECT_BYTE = 15
    TURN_CHANNEL_ON_BYTE = 12

    def __init__(self, chip_select:int, ldac: int, sck: int, mosi: int, miso:int):
        self.spi = SPI(1, 5000000, sck=Pin(sck, Pin.OUT), mosi=Pin(mosi, Pin.OUT), miso=Pin(miso), polarity=0, phase=0, firstbit=SPI.MSB)

        self.chip_select = Pin(chip_select)
        self.ldac = Pin(ldac)



        self.init()

    def init(self):
        self.chip_select.init(self.chip_select.OUT, value=1)
        self.ldac.init(self.ldac.OUT, value=0)
        time.sleep_ms(120)

    def _write(self, data: int):
        self.ldac.value(1)
        self.chip_select.value(0)
        self.spi.write(bytearray(bin(data)))
        self.chip_select.value(1)
        self.ldac.value(0)

    def set_voltage(self, voltage: int):
        #command = 0 << 15  # channel A
        #command = command | (1 << 12)  # turn on
        #command = command | (0 << 13)  # set gain to high
        #value = voltage >> (12 - 12)  # second 12 is bit resolution (12-bit_resolution), set voltage
        command = voltage
        
        #print("command: {}".format(command))
        #print("bin: {}".format(bin(command)))
        dac._write(command)
        #import sys
        #print(sys.getsizeof(bin(command)))

dac = MCP4822(5, 2, 18, 23, 19)

dac.set_voltage(2000)
