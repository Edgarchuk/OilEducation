from tkinter import *
import random

class SimulationTest:
  def __init__(self, parent, test) -> None:
    self.test = test
    self.actions = random.shuffle(test)
    self.answer = []
    
    self.window = Toplevel(parent)

    self.answerLabel = Label(self.window, text="Ответ")
    self.answerLabel.grid(row=0, column=0, sticky=W)

    self.answerFrame = Frame(self.window)
    self.answerFrame.grid(row=1, column=0, sticky=N+S)

    self.answerScrollbar = Scrollbar(self.answerFrame, orient="vertical")
    self.answerScrollbar.pack(side=RIGHT, fill=Y)

    self.answersList = Listbox(self.answerFrame, yscrollcommand=self.answerScrollbar.set)
    self.answersList.pack(expand=True, fill=Y)

    self.answerScrollbar.config(command=self.answersList.yview)

    self.actionsLabel = Label(self.window, text="Действия")
    self.actionsLabel.grid(row=0, column=1, sticky=W)

    self.actionsFrame = Frame(self.window)
    self.actionsFrame.grid(row=1, column=1)

    self.actionsScrollbar = Scrollbar(self.actionsFrame, orient="vertical")
    self.actionsScrollbar.pack(side=RIGHT, fill=Y)

    self.actionsList = Listbox(self.actionsFrame, yscrollcommand=self.actionsScrollbar.set)
    self.actionsList.pack(expand=True, fill=Y)

    self.actionsScrollbar.config(command=self.actionsList.yview)

    for item in self.actions:
      self.actionsList.insert(END, item)
    self.actionsList.update()