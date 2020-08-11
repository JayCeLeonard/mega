
import serial
#git test 1
class PIN:
    def __init__(self,pin_num,pin_color):
        self.num = pin_num #int
        self.color = pin_color #string
    
    def Print(self):
        print(self.color,self.num)
    #change color
    #copy constructor

class CONNECTOR:
    def __init__(self,name):
        self.pins = connectors(name)
    def set_out(self):
        [pin.Print() for pin in self.pins]
    def set_in(self):
        [pin.Print() for pin in self.pins]
        #will set the pins in the conectotro to a input

class RECIVER_TRANSIMTER(CONNECTOR):
    def talk(self):
       
        # are ouy ready
        # hear is info
        # did you get what I said
    def listen(self):
        
        # what?
        # listen to tranmiter
        # ready to test
     





default_connecotr = {PIN(1,"brown"),PIN(2,"not brown")}

#set this to take in a string later
def connectors(arg):
    ARR = {
        1:default_connecotr
    }

    return list (ARR.get(arg))
