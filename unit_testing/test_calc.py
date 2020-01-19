import unittest
import calc
# The calc.py module can import because it is in local directory
# Documentation on unittest assert methods can be found here:
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class TestCalc(unittest.TestCase):

   # Test must be named test_ or it will not run as a test in unittest
   def test_add(self):
      result = calc.add(10, 5)
      self.assertEqual(result, 15)
      # Edge case testing is important for coverage
      self.assertEqual(calc.add(1, -1), 0)
      self.assertEqual(calc.add(-1, -1), -2)

   def test_subtract(self):
      self.assertEqual(calc.subtract(10, 5), 5)
      self.assertEqual(calc.subtract(1, -1), 2)
      self.assertEqual(calc.subtract(-1, -1), -0)
   
   def test_multiply(self):
      self.assertEqual(calc.multiply(10, 5), 50)
      self.assertEqual(calc.multiply(1, -1), -1)
      self.assertEqual(calc.multiply(-1, -1), 1)

   def test_divide(self):
      self.assertEqual(calc.divide(10, 5), 2)
      self.assertEqual(calc.divide(-1, 1), -1)
      self.assertEqual(calc.divide(-1, -1), 1)
      self.assertEqual(calc.divide(5, 2), 2.5)

      # This test for an error so needs a error input to pass
      self.assertRaises(ValueError, calc.divide, 10, 0)

      # Test error with context manager allows to call function naturally, still needs error input to pass
      with self.assertRaises(ValueError):
        calc.divide(10, 0) 

   def test_floor_divide(self):
      self.assertEqual(calc.floor_divide(1, -1), -1)
      self.assertEqual(calc.floor_divide(-1, -1), 1)
      # Floor divide returns whole integers
      #self.assertEqual(calc.floor_divide(5, 2), 2.5)
      self.assertEqual(calc.floor_divide(5, 2), 2)
  

if __name__ == '__main__':
   unittest.main()
     
