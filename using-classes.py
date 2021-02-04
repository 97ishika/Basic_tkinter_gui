
from tkinter import *
class My_buttons:

    def __init__(self, root_one):

        frame = Frame(root_one)
        frame.pack()

        self.print_button = Button(frame, text = "Click Here", command = self.print_msg)
        self.print_button.pack()

        self.quit_button = Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side = LEFT)


    def print_msg(self):
        print("Button Clicked")

root = Tk()
b = My_buttons(root)

root.mainloop()




