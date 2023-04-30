from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def mi_to_km():
    miles = float(inpt.get())
    km = miles * 1.60934
    kilometer_num_label.config(text=round(km, 2))


inpt = Entry(width=10)
inpt.grid(row=0, column=1, pady=10)

miles_label = Label(text="miles")
miles_label.grid(row=0, column=2, pady=10)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

kilometer_num_label = Label(text="0")
kilometer_num_label.grid(row=1, column=1)

kilometer_label = Label(text="kilometers")
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=mi_to_km)
calculate_button.grid(row=2, column=1, pady=10)

window.mainloop()
