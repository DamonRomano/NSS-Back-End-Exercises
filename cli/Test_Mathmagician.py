import unittest
from mathmagician import *

@classmethod
def setUp(self)
  self.magician = Magician()

def test_integer_generator_works(self):
  integer = self.generate_integers(10)
  self.assertEqual([0,1,2,3,4,5,6,7,8,9], integer)

def test_Fibonacci_Sequence_generator_works(self):
  fibonacci_sequence = self.generate_fibonacci_sequence(10)
  self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], fibonacci_sequence)

def test_prime_number_generator_works(self):
  prime_numbers = self.generate_prime_numbers(7)
  self.assertEqual([2,3,5,7,11,13,17,19,23, 29], prime_numbers)
