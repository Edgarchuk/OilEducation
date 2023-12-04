from tkinter import *
from View.SimulationView import SimulationView

class SimulationList:
  def __init__(this, parent, simulations):
    this.win = Toplevel(parent)
    this.win.title("Симуляции")
    this.win.attributes('-fullscreen', True)
    this.win['background']='cornsilk3'
    btn = Button(this.win, text='Меню', bg='#A39B8B', fg='white')
    btn.pack(anchor=NE, padx=5, pady=5)


    def openSimulation(simulation):
      this.currentSimulation = SimulationView(simulation=simulation)
      this.win.withdraw()

    simulations = list(map(
      lambda simulation: Button(this.win, text=simulation.name, command= lambda: openSimulation(simulation), bg='#A39B8B', width=80, height=5), 
      simulations
      
    ))
    for simulation in simulations:
      simulation.pack(anchor=NW, padx=10, pady=5)