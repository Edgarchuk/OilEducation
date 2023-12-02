from tkinter import *

from View.SimulationTest import SimulationTest

class SimulationView:
  def __init__(self, simulation) -> None:
    self.window = Toplevel()
    self.window.title(simulation.name)
    self.window.attributes('-fullscreen', True)

    self.simulation = simulation

    self.test = Button(self.window, text="Tecтирование", command=self.openTest)
    self.test.pack(side="top", padx=8)

    self.education = Button(self.window, text="Обучение")
    self.education.pack(side="top", padx=8)

  def openTest(self):
    self.testView = SimulationTest(self.window, self.simulation.test)