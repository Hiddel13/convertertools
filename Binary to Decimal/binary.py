from tkinter import *  ##imports tkinter

top = Tk()
top.geometry("400x300")
top.title("Binary to Decimal converter")
label = Label(top, text = "", font =("Arial", 14))

def convert():
    midput = inp.get()
    lmp = len(midput)
    total = 0
    b = 2 ** lmp / 2
    for letters in midput:
        p = int(letters)
        if p == 1:
            total = total + b
            b = b / 2
        if p == 0:
            b = b / 2

    label.config(text = total)
    label.pack()

title = Label(top, text = "Binary to Decimal converter", font =("Arial", 16))
inp = Entry(top, font =("Arial", 15))
button = Button(top, text = "Convert", command = convert, font =("Arial", 14))
title.pack()
inp.pack()
button.pack()
label.pack()


top.mainloop()