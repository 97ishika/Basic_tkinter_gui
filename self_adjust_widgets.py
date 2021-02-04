from tkinter import *
root = Tk()

label_fn = Label(root, text = "First Name", bg = "Red", fg = "White")
label_fn.pack(fill = X)
label_ln = Label(root, text = "Last Name", bg = "Blue", fg = "White")
label_ln.pack(side = LEFT, fill = Y)

root.mainloop()
