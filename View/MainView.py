from tkinter import *
from tkinter import ttk
from Model.SimulationModel import Simulation

from View.SimulationList import SimulationList
from View.VerticalMenu import *
class MainView:
  def __init__(this, title):    
    this.window = Tk()
    this.window.title('Меню')
    this.window.attributes('-fullscreen', True)
    this.window['background']='#07020D'
    this.loadViews()

  def loadViews(this):
    this.menu = VerticalMenu(title="Меню", parent=this.window, height=850, width=300)
    this.menu.frame.grid(row=0, column = 0, padx = 8, pady = 8)
    this.menu.setButtons([VerticalMenu.ButtonOption(title="Симуляции", command=this.openSimulationWindow),VerticalMenu.ButtonOption(title="Выход", command=this.window.destroy)])

  def openSimulationWindow(this):
    this.simulation = SimulationList(this.window, [Simulation("test", ["one", "two", "three"], NONE)])

  def mainloop(this):
    this.window.mainloop()