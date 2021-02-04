from tkinter import *
root = Tk()

def do_something():
    print("You clicked something")

button1 = Button(root, text = "Click Here", command = do_something)
button1.pack()

root.mainloop()