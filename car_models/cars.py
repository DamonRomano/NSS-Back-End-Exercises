def __init__(self):
  pass

def read_car_makes(self):
  with open("car-makes", "r") as make_file:
    car_makes = { make[:-1] for make in make_file }

  return car_makes


def read_car_models(self):
  with open("car-models", "r") as model_file:
    car_models = { }

  return car_models

def create_collection(self):



def read_car_models(self):
  with open("car-models", "r") as model_file:
    car_models = {model}



for make in makes:
  collection[make] = []
  for model in models:
    if make [0] == model.split("=")[0]:
      self.collection[make].append(model.split("=")[1])

print(self.collection)