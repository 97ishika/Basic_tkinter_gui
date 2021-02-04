from tkinter import *

def function1():
    print("Menu item is clicked")

root = Tk()

myMenu = Menu(root)
root.config(menu = myMenu)

sub_menu = Menu(myMenu)

myMenu.add_cascade(label = "File", menu = sub_menu)
sub_menu.add_command(label = "Project", command = function1)
sub_menu.add_command(label = "Save", command = function1)
sub_menu.add_separator()
sub_menu.add_command(label = "Settings", command = function1)

edit_menu = Menu(myMenu)

myMenu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function1)
edit_menu.add_command(label = "Cut", command = function1)


root.mainloop()