
from connectors import CONNECTOR
from connectors import PIN
#array of pins 
# funtion that set up the pins that will be tested
def init_pins_in(ARRAY):
    [pin.Print() for pin in ARRAY ]

# fintion what will test the pins for all pin in the list
def test_pins_in(ARRAY):
    for pin in ARRAY.pins :
        counter = 0
        button_counter = 0
        while counter <100000:
            counter += 1
            button_counter += 1 
        if button_counter < 100000:
            print("Pin:", pin.color, "fail")
        else:
            print("Pin:", pin.color ,"fail")

def main():

    

if __name__ == "__main__" :
    main()