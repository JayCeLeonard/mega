import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 7
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,False)

print(GPIO.input(7))
