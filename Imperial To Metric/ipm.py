from tkinter import *

top = Tk()

i = StringVar(top)
i.set("Please Select an Option")

def convert():
    print (i.get(), entry1.get())
    option = i.get()
    inp = float(entry1.get())
    out = float(0)
    if (option == "Feet to Meter"):
        out = float(inp / 3.281)
        output = Label(top, text = (out, "Meter"), font = ("Arial", 20))
        output.pack()
    if (option == "Inch to Centimeter"):
        out = float(inp * 2.54)
        output = Label(top, text = (out, "Centimeter"), font = ("Arial", 20))
        output.pack()
    if (option == "Mile to Kilometer"):
        out = float(inp * 1.609)
        output = Label(top, text = (out, "Kilometer"), font = ("Arial", 20))
        output.pack()
    if (option == "Ounces to Grams"):
        out = float(inp * 28.35)
        output = Label(top, text = (out, "Grams"), font = ("Arial", 20))
        output.pack()
    if (option == "Pounds to Kilograms"):
        out = float(inp / 2.205)
        output = Label(top, text = (out, "Kilogram"), font = ("Arial", 20))
        output.pack()
    if (option == "Fahrenheit to Celsius"):
        out = float((inp - 32) * 5/9)
        output = Label(top, text = (out, "Celcius"), font = ("Arial", 20))
        output.pack()
    if (option == "Yard to Meters"):
        out = float(inp / 1.094)
        output = Label(top, text = (out, "Meter"), font = ("Arial", 20))
        output.pack()
    if (option == "Nautical Mile to Kilometers"):
        out = float(inp / 1.852)
        output = Label(top, text = (out, "Kilometer"), font = ("Arial", 20))
        output.pack()
    if (option == "Inch to Millimeter"):
        out = float(inp * 25.4)
        output = Label(top, text = (out, "Millimeter"), font = ("Arial", 20))
        output.pack()

    
    
top.title("Imperial to Metric measurements converter")
top.geometry('450x400')

Label1 = Label(top, text = "Imperial to Metric", font = ("Arial", 30))
Label2 = Label(top, text = "Input:", font = ("Arial", 13))

menu = OptionMenu(top, i, "Feet to Meter", "Inch to Centimeter", "Mile to Kilometer", "Ounces to Grams", "Pounds to Kilograms", "Fahrenheit to Celsius", "Yard to Meter", "Nautical Mile to Kilometers", "Inch to Millimeter")
menu.config(font = ("Arial", 13))

button = Button(top, text = "Convert", command=convert, font=("Arial", 13))
entry1 = Entry(top, bd =3, font = ("Arial", 15))

Label1.pack()
menu.pack()
Label2.pack()
entry1.pack()
button.pack()

    
top.mainloop()