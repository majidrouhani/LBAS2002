from tkinter import *
from tkinter import messagebox

def search():
    messagebox.showinfo("Info", regnr.get())

root = Tk()

regnr_label = Label(root, text="Regnr:")

regnr = StringVar()  # Definerer en tekstvariabel for tekstfeltet
regnr_entry = Entry(root, textvariable=regnr)

search_button = Button(root, text="Søk", command=search)

regnr_label.grid(column=1, row=0, padx=2, pady=2)
regnr_entry.grid(column=2, row=0, padx=2, pady=2)
search_button.grid(column=2, row=1, columnspan=2, padx=2, pady=2)


root.mainloop()
