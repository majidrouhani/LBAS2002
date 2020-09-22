from tkinter import *



root = Tk()

name_label = Label(root, text="Navn:")

name = StringVar()

name_label.grid(column=0, row=0, padx=2, pady=2)

name_entry = Entry(root, textvariable=name)
name_entry.grid(column=1, row=0, padx=2, pady=2)

root.mainloop()



