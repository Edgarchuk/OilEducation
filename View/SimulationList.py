from tkinter import *

from View.SimulationView import SimulationView

class SimulationList:
  def __init__(this, parent, simulations):
    this.window = Toplevel(parent)
    this.window.title("Симуляции")
    this.window.geometry("300x300")

    def openSimulation(simulation):
      this.currentSimulation = SimulationView(simulation=simulation)

    simulations = list(map(
      lambda simulation: Button(this.window, text=simulation.name, command= lambda: openSimulation(simulation)), 
      simulations
    ))
    for simulation in simulations:
      simulation.pack(side="top")