import tkinter

def calculate():
    km = float(input.get())/0.621371
    km_val_label.config(text=str(round(km, 2)))

window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")

#Input
input = tkinter.Entry(width=7)
input.grid(column=1, row=0)

#Labels
miles_label = tkinter.Label(text=" Miles")
miles_label.grid(column=2, row=0)

is_label = tkinter.Label(text="is equal to")
is_label.grid(column=0, row=1)

km_label = tkinter.Label(text=" Km")
km_label.grid(column=2, row=1)

km_val_label = tkinter.Label(text="0")
km_val_label.grid(column=1, row=1)

#Button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()