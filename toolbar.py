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

toolbar = Frame(root, bg = "Pink")

insert_button = Button(toolbar, text = "Insert Files", command = function1)
insert_button.pack(side = LEFT, padx = 2, pady = 3)

print_button = Button(toolbar, text = "Print", command = function1)
print_button.pack(side = LEFT, padx = 2, pady = 3)

toolbar.pack(side = TOP, padx = 2, pady = 3)

status = Label(root, text = "This is the status", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)


root.mainloop()