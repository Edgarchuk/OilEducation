from tkinter import *

class VerticalMenu:
    def __init__(this, title, parent,  height, width):
        this.frame = Frame(parent, height=height, width=width, bg='#F1E9DB')
        this.frame.pack_propagate(0)
        this.name_label = Label(this.frame, text=title, bg='#F1E9DB')
        this.name_label.pack(side=TOP)

    def setButtons(this, buttonOptions):
        for buttonOption in buttonOptions:
            button = buttonOption.getButton(this.frame)
            button.pack(side=TOP, pady = 20)

    class ButtonOption:
        def __init__(this, title, command):
            this.title = title
            this.command = command

        def getButton(this, parent):
            button = Button(parent, text=this.title, command=this.command, bg='#A39B8B', width=30, height=3, fg='white')
            return button
