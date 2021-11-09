"""
Øving i enkel GUI.
Programmet ber brukeren om å skrive en melding. Deretter vises melding til bruker via en dialogboks.
"""
from tkinter import Tk, Label, StringVar, Entry, Button,messagebox


def show_message():
    messagebox.showinfo("Melding","Hei "+name.get())


# Opprett hovedvindu
root = Tk()

# Oppretter en ledetekster
name_label = Label(root, text="Navn:")


# Oppretter tekstfelter brukeren kan søke fra
name = StringVar()  # Definerer en tekstvariabel for tekstfeltet
name_entry = Entry(root, textvariable=name)


# Plasserer widget'ene i vinduet i et rutenett (grid)
name_label.grid(column=0, row=0, padx=2, pady=2)
name_entry.grid(column=1, row=0, padx=2, pady=2)

ok_message = Button(root, text="OK", command=show_message)
ok_message.grid(row=1, column=1)


# Starter GUI'et
root.mainloop()
