"""
Starting Point for Python GUI using Tkinter based on YouTube Tutorial
"""

from tkinter import *
from PIL import ImageTk, Image

#pip install Pillow

# global variable 

# root has to come first -- start of window
root = Tk()
root.title("STUFF TO FOLLOW")
root.iconbitmap('C:/Users/feathers/Desktop/concrete_QQQ_icon.ico')
root.geometry("800x800")

button_quit = Button(root, text="exit this", command = root.quit)
button_quit.pack()

#need to import to use jpg, png
my_img = ImageTk.PhotoImage(Image.open("C:/Users/feathers/Desktop/Concrete.jpg"))
my_label = Label(image=my_img)
my_label.pack()


root.mainloop()