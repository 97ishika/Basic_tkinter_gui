from tkinter import *
root = Tk()

upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack(side = BOTTOM)

button1 = Button(upFrame, text = "Click Here", fg = "Green")
button2 = Button(downFrame, text = "Don't Click Here", fg = "Red")

button1.pack()
button2.pack()

root.mainloop()
