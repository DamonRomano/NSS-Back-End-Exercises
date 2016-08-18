import unittest
import zoolandia

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_animal_creation(self):
    bob = zoolandia.Betta('orange', 'Bob')
    self.assertIsInstance(bob, zoolandia.Betta)


    self.assertEqual(bob.species.color, 'orange')
    self.assertEqual(bob.name, 'Bob')
    self.assertIsInstance(bob, zoolandia.Animal)
    self.assertIsInstance(bob.species, zoolandia.Species)
    self.assertIsInstance(bob.species, zoolandia.BettaTrifasciata)

  def test_species_none_default(self):
    a_animal = zoolandia.Animal('name', 'species')
    self.assertEqual(a_animal.species, None)


class TestSpecies(unittest.TestCase):

  def test_common_name_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.common_name, '')

  def test_geo_region_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.geo_region, '')


class TestHabitat(unittest.TestCase):

  def test_name_empty_string_default(self):
    habitat = zoolandia.Habitat()
    self.assertEqual(habitat.name, '')

  def test_members_set_default(self):
    habitat = zoolandia.Habitat()
    self.assertIsInstance(habitat.members, set)

  def test_add_member(self):
    aquarium = zoolandia.Aquarium('freshwater')
    bob.zoolandia.Betta('orange', 'bob')
    james.zoolandia.Betta('blue', 'James')
    aquarium.add_member(bob)
    self.assertIn(bob, aquarium.members)
    aquarium.add_member(james)
    aquarium.remove_member(james)

    self.assertNotIn(james, aquarium.members)


class TestWalking(unittest.TestCase):

  def test_legs_zero_default(self):
    walking = zoolandia.Walking()
    self.assertEqual(walking.legs, 0)

  def test_walk_speed_zero_default(self):
    walking = zoolandia.Walking()
    self.assertEqual(walking.walk_speed, 0)


class TestFlying(unittest.TestCase):

  def test_wings_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.wings, 0)

  def test_wing_span_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.wing_span, 0)

  def test_air_speed_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.air_speed, 0)


class TestSwimming(unittest.TestCase):

  def test_appendages(self):
    swimming = zoolandia.Swimming()
    self.assertFalse(swimming.fins)
    self.assertFalse(swimming.flippers)
    self.assertFalse(swimming.web_feet)
    self.assertFalse(swimming.swim_speed)

  def test_swim_speed_zero_default(self, swimming):
    swimming = zoolandia.swimming()
    self.assertEqual(swimming.swim_speed, 0)


if __name__ == '__main__':
    unittest.main()

