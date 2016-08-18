from csolid import CircularSolid

class Cylinder(CircularSolid):

  def __init__(self, height, radius):
    super().__init__(height = height, radius = radius)

  def area(self):
    super().area()