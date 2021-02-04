from tkinter import *
root = Tk()

label_fn = Label(root, text = "First Name")
label_ln = Label(root, text = "Last Name")

entry_fn = Entry(root)
entry_ln = Entry(root)

label_fn.grid(row = 0, column = 0)
label_ln.grid(row = 1, column = 0)

entry_fn.grid(row = 0, column = 1)
entry_ln.grid(row = 1, column = 1)

root.mainloop()
