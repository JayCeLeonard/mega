import serial
import RPi.GPIO as GPIO
import time
import struct

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)#if you are using periferil pins as GPIO pins like i am, you will need to disable warnings


input_pins = list([7,11,13,15,19,21,23,29,31,33,35,37,12,16,18,22,24,26,32,36,38,40])

ser = serial.Serial( # this is the set up for the uart
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 500,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

class PIN: #this is a pin object that holds everything you neen to know
    def __init__(self, OUT_PINS , IN_PIN, COLOR):
        self.inPin = int(IN_PIN)
        self.outPin = int(OUT_PINS) # this is the value that will be in a bit shift >> opeator
        self.color = str(COLOR)

class CONNECTOR:
    def __init__(self,name): # pins has to  be a list
        self.pins = connectors(name)
        self.name = name

        for pin in self.pins :
            GPIO.setup(input_pins[pin.inPin],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    def read_input(self,expected_pin):
        
        Pass = False
        x = input_pins[expected_pin]
        if ( GPIO.input(x) == 1):
            x = str(input_pins[expected_pin])
            return x + " pass"
        else:
            
            for pin in self.pins:
                x = input_pins[pin.inPin]
                if(GPIO.input(x)):
                    x = str(expected_pin)
                    y = str(pin.inPin)
                    return  str("pin " + x + ": connected to pin " + y)
            if (index == 100):
                x = str(expected_pin)
                return  str("pin " + x + ": no conection")

    def test(self): #this function set
        temp = list()
        for pin in self.pins:
            x = str(pin.inPin)
            x += '\n'
            ser.write(x.encode())
            time.sleep(.25)
            temp.append(self.read_input(pin.inPin))
        return temp

    def __write(self):
        print("write")

#every time you make a new conecotr for have to to this :(
default_connecotr = list([PIN(0,0,"brown"),PIN(1,1,"not brown"),PIN(2,2,"brown"),PIN(3,3,"brown"),PIN(4,4,"not brown"),
PIN(5,5,"brown"),PIN(6,6,"brown"),PIN(7,7,"brown"),PIN(8,8,"not brown"),PIN(9,9,"brown"),PIN(10,10,"brown"),
PIN(11,11,"brown"),PIN(12,12,"not brown"),PIN(13,13,"brown"),PIN(14,14,"brown"),PIN(15,15,"not brown"),PIN(16,16,"brown"),
PIN(17,17,"brown"),PIN(18,18,"not brown"),PIN(19,19,"brown"),PIN(20,20,"brown"),PIN(21,21,"not brown")])

HermN3_connector = list([PIN(0,0,"brown"),PIN(1,1,"not brown"),PIN(3,3,"brown"),PIN(6,6,"brown"),PIN(9,9,"brown"),PIN(12,12,"not brown")])

#i dont like how the dictionary is set up, should pull data from a shared header file. this data has to be identical to the list_box in the app
def connectors(arg):
    ARR = {
        'Fish': default_connecotr,
        'HermN3': HermN3_connector,
        'Truck-Harnes': default_connecotr,
        "ODOT-F12-0003": default_connecotr,
        "ff02-Line-ST-jump": default_connecotr,
        "Camper Speaker Jumpers": default_connecotr,
        "Schwant": default_connecotr,
        "Schwintek": default_connecotr,
        "Camper Hernac": default_connecotr,
        "floor to Truck Hermac": default_connecotr
    }

    x = ARR.get(arg,default_connecotr)
    return x