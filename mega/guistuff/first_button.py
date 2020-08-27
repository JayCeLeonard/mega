from guizero import App, PushButton,Box, TextBox,Text,ListBox,ButtonGroup,yesno,Window
from connectors import CONNECTOR, PIN
import os

# for the love of got clean this shit up, all of the functions for the app should be in their oun library
#did the update feature actually work?

def updatefunc():
    os.system('gitup')
    os.system('git merge -m"standard update"')

app = App(title = 'meeting console', width = 750, height = 750, layout='grid')
app.tk.attributes("-fullscreen",True)
os.system('python blink_setup.py')

window = Window(app,title= "restart the box")
window.full_screen= True # this dont fukin wrk you btch

windowtxt = Text(window, text="please restart the box (flip the power switch on and off)", size= 10)
window.hide()

def do_nothing():
    x = CONNECTOR(button.text)
    y = x.test()
    input_box.clear()
    for pin in y:
        input_box.append(pin)

def bsfunc():
    input_box.clear()
    resultText.text = "running"
    input_box.append("running test...")
    app.update()
    input_box.after(0, do_nothing)

# have a yes no box connected to the app
# if no is selected do nothing
#if yes
    #run the update bs
    #find out how to restart the app
    #there is no place like home

def restart():
    if(yesno("Update", "Did you mean to press the update button?")):
        os.system('gitup')
        os.system('git merge -m"standard update"')
        window.show()

def list_sel(value):
    button.text= value



button = PushButton(app,text ="No test Harness selected", command=bsfunc, grid=[0,0])
updatebutton = PushButton(app,text ="update", command=restart, grid=[0,1])

text = Text(app, text="click on the tester that you want in the box below", grid=[100,0])
resultText = Text(app, grid=[50,0],text="pick connector")

input_box = TextBox(app,grid=[60,50],multiline=True,height="fill",width="fill")
listbox = ListBox(app, items=["Fish","HermNS","Truck Harnes","ODOT-F12-0003","ff02-Line-ST-jump","Camper Speaker Jumpers","Schwant","Schwintek","Camper Hernac","floor to Truck Hermac"],command = list_sel,grid=[0,50],scrollbar=True)
input_box.text = "select the test"


listbox.text_size =20
app.display()
