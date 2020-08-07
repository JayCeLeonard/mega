import serial
import time



ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0

    
if __name__ == "__main__" :
   while(1):
        
        ser.write('Write counter: %d \n'%(counter))
        counter += 1
        time.sleep()
        #data_left = ser.inWaiting()  # Get the number of characters ready to be read
       # Do the read and combine it with the first character
        print(counter)
       
