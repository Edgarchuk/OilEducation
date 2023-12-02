from tkinter import *
from Model.SimulationModel import Simulation

from View.SimulationList import SimulationList
class MainView:
  def __init__(this, title):    
    this.window = Tk()
    this.window.title(title)
    this.window.geometry("1000x1000")
    this.loadViews()

  def loadViews(this):
    this.menu = Frame(this.window)
    this.menu.grid(row=0, column = 0, padx = 8, pady = 8)

    this.button = Button(this.window, text="Симуляции", command=this.openSimulationWindow)
    this.button.grid(row=0, column = 0, padx = 8, pady = 8)

    this.imageFrame = Frame(this.window)
    this.imageFrame.grid(row=0, column = 1, padx = 8, pady = 8)

    this.imageData = PhotoImage(file="Assets/logo.png")
    this.image = Label(this.imageFrame,image=this.imageData)
    this.image.grid(row=0, column = 0, padx = 8, pady = 8)

  def openSimulationWindow(this):
    this.simulation = SimulationList(this.window, [Simulation("test", ["one", "two", "three"], NONE)])

  def mainloop(this):
    this.window.mainloop()