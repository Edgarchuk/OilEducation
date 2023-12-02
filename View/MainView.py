from tkinter import *
from tkinter import ttk
from Model.SimulationModel import Simulation

from View.SimulationList import SimulationList
from View.VerticalMenu import *
class MainView:
  def __init__(this, title):    
    this.window = Tk()
    this.window.title(title)
    this.window.attributes('-fullscreen', True)
    this.loadViews()

  def loadViews(this):
    title = "text"
    this.menu = VerticalMenu(title="Меню", parent=this.window, height=100, width=100)
    this.menu.frame.grid(row=0, column = 0, padx = 8, pady = 8)
    
    
  def openSimulationWindow(this):
    this.simulation = SimulationList(this.window, [Simulation("test", ["one", "two", "three"], NONE)])

  def mainloop(this):
    this.window.mainloop()