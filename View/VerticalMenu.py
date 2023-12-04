from tkinter import *

class VerticalMenu:
    def __init__(this, title, parent,  height, width):
<<<<<<< Updated upstream
        this.frame = ttk.Frame(parent, height=height, width=width)
        this.name_label = ttk.Label(this.frame, text=title)
=======
        this.frame = Frame(parent, height=height, width=width, bg='#F1E9DB')
        this.frame.pack_propagate(0)
        this.name_label = Label(this.frame, text=title, bg='#F1E9DB')
>>>>>>> Stashed changes
        this.name_label.pack(side=TOP)

    def setButtons(this, buttonOptions):
        pass

    class ButtonOption:
        def __init__(this, title, command):
            pass

<<<<<<< Updated upstream
        def getButton(this):
            pass
=======
        def getButton(this, parent):
            button = Button(parent, text=this.title, command=this.command, height= 2, width=10, bg='#A39B8B')
            return button
>>>>>>> Stashed changes
