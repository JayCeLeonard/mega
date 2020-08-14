
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
#did it work?
value =1 ^ GPIO.input(7)
print(value)

GPIO.output(7,value)

