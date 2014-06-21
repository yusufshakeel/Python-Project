from tkinter import *       #import all definitions (classes, functions, constants) from tkinter module

def btnOKClicked():
    print("OK button is clicked!")

window = Tk()       #create a window
btnOK = Button(window, text="OK", fg="red", command=btnOKClicked)
btnOK.pack()
window.maniloop()
