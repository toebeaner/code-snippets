class example:
  def __init__(self, breed = None, name = None):
    self.breed = breed
    self.name = name

  def print_all(self):
    return f"Breed - {self.breed}\nName - {self.name}" # line 9/10
  
  def view(self):
    class data(object):
      breed = self.breed # line 9
      name = self.name # line 10
    return data
