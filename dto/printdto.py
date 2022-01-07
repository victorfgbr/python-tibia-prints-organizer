def __init__(self):
  return self

class PrintDto:
  def __init__(self, fileName):
    self.fileName = fileName
    infos = fileName.removesuffix(".png").split("_")
    self.date = infos[0]
    self.time = infos[1]
    self.characterName = infos[2]
    self.type = infos[3]

  def __str__(self):
    return (f'{self.characterName} prints {self.type} at {self.date}')
