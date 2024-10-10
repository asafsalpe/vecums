from ctypes import resize
from email.mime import image
import tkinter as tk
import datetime
from PIL import Image, ImageTk

master = tk.Tk()
master.geometry("500x500")
master.configure()

nameInput = tk.Entry(master)
nameInput.grid(row=1, column=1)

yearInput = tk.Entry(master)
yearInput.grid(row=2, column=1)

monthInput = tk.Entry(master)  
monthInput.grid(row=3, column=1)

dayInput = tk.Entry(master)  
dayInput.grid(row=4, column=1)

namelbl = tk.Label(master, text="Vārds: ")
namelbl.grid(row=1, column=0)

yearlbl = tk.Label(master, text="Dzimšanas gads: ")
yearlbl.grid(row=2, column=0)

monthlbl = tk.Label(master, text="Mēnesis: ")
monthlbl.grid(row=3, column=0)

daylbl = tk.Label(master, text="Diena: ")
daylbl.grid(row=4, column=0)

aprekinat = tk.Button(master, text="Aprēķināt vecumu", command=lambda: aprekinat_vecumu())
aprekinat.grid(row=5, column=1)

listbox = tk.Listbox(master)
listbox.grid(row=6, column=1)
listbox.configure(width=50, height=5)

img = Image.open("sunŽozefīne.jpg")
img = img.resize((224,168))
img_tk = ImageTk.PhotoImage(img)
img_label = tk.Label(master, image=img_tk)
img_label.grid(row=0, column=1)

def aprekinat_vecumu():
    today = datetime.date.today()
    try:
        year = int(yearInput.get())
        month = int(monthInput.get()) if monthInput.get() else 1
        day = int(dayInput.get()) if dayInput.get() else 1

        birth_date = datetime.date(year, month, day)

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        listbox.delete(0, tk.END)
        listbox.insert(tk.END, f"Sveiki, mani sauc {nameInput.get()} un man ir {age} gadi!")
    except ValueError:
        listbox.delete(0, tk.END)
        listbox.insert(tk.END, "Lūdzu, ievadiet derīgas vērtības.")

master.mainloop()