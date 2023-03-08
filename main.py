from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


def on_click():
    miles = int(input.get())
    dis_km = miles * 1.61
    show_km.config(text=f"{dis_km} kilometers")


# entry

input = Entry(width=10)
input.grid(column=1, row=0)

# Label

intro = Label(text="Miles", font=("Ariel", 10, "normal"))
intro.grid(column=2, row=0)
conv = Label(text="is converted to", font=("Ariel", 10, "normal"))
conv.grid(column=0, row=1)
show_km = Label(text="0", font=("Ariel", 10, "normal"))
show_km.grid(column=1, row=1)
km = Label(text="kilometers", font=("Ariel", 10, "normal"))
km.grid(column=2, row=1)

# button

button = Button(text="Convert", command=on_click)
button.grid(column=1, row=2)

window.mainloop()
