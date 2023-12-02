from tkinter import *
from tkinter import ttk

class VerticalMenu:
    def __init__(this, title, parent,  height, width):
        this.frame = ttk.Frame(parent, height=height, width=width)
        this.frame.pack_propagate(0)
        this.name_label = ttk.Label(this.frame, text=title)
        this.name_label.pack(side=TOP)

    def setButtons(this, buttonOptions):
        for buttonOption in buttonOptions:
            button = buttonOption.getButton(this.frame)
            button.pack(side=TOP, pady = 20, fill=X)

    class ButtonOption:
        def __init__(this, title, command):
            this.title = title
            this.command = command

        def getButton(this, parent):
            button = Button(parent, text=this.title, command=this.command, height= 2, width=10)
            return button
