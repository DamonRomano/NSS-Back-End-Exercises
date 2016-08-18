def __init__(self):
  pass

def area(self, width = 0, height = 0, depth = 0, radius = 0):
  area = 0

  if radius > 0:
    if height > 0:
      area = radius**2 * pi * height
    else:
      area = radius**2 * pi

  elif