class SimulationEducation:

  class EducationItem:
    def __init__(self, text, imagePath) -> None:
      self.text = text
      self.imagePath = imagePath
  def __init__(self, items) -> None:
    self.items = items

class SimulationTest:
  def __init__(self, actions):
    self.actions = actions

class Simulation:
  def __init__(this, name, test, education):
    this.name = name
    this.test = test
    this.education = education
    