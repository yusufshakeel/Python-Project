from tkinter import *       #import all definitions (classes, functions, constants) from tkinter module

window = Tk()       #create a window
label = Label(window, text="Hello World!")  #create a label
button = Button(window, text="Click Me")    #create a button
label.pack()    #place label in the windows
button.pack()   #place button in the window
window.mainloop()   #create an event loop
