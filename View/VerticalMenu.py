from tkinter import *
from tkinter import ttk

class VerticalMenu:
    def __init__(this, title, parent,  height, width):
        this.frame = ttk.Frame(parent, height=height, width=width)
        this.name_label = ttk.Label(this.frame, text=title)
        this.name_label.pack(side=TOP)

    def setButtons(this, buttonOptions):
        pass

    class ButtonOption:
        def __init__(this, title, command):
            pass

        def getButton(this):
            pass
