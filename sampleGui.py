from tkinter import *

# global variable 

# root has to come first -- start of window
root = Tk()
root.title("Simple Gui ")

# creating a label widget, and then use pack() to put in first available spot, or grid with row, column
myLabel = Label(root, text = "STARTING UP")
myLabel2 = Label(root, text = "YADA")

myLabel.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)

# Input widget, e.get() to grab input
e = Entry(root, width = 50)
e.grid(row = 90, column = 90)
e.insert(0,"Enter your gosh damn name here")
#e.delete(0, END) to delete everything


#button creation, set state to DISABLED to make unclickable, padx gives space on both sides of text
def myClick():
    myLabel = Label(root, text = "Hello" + e.get())
    myLabel.grid(row = 14, column = 14)

# need to use Lambda: function(parameter) to add a parameter
myButton = Button(root, text = "LETS GO", padx = 50, pady = 50, command = myClick, fg = "blue", bg = "red")
myButton.grid(row = 12, column = 12)




# event loop
root.mainloop()