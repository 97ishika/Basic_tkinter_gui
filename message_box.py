from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title", "This is awesome")

response = tkinter.messagebox.askquestion("Do you like biryani or not")
if response == 'yes':
    print("I'll take you to Aminia, my friend")
else:
    print("Please choose another friend")

root.mainloop()
