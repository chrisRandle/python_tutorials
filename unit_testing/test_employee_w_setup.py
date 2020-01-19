import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

   def setUp(self):
      # Must set as instance attributes with self.attribute
      self.emp_1 = Employee('Corey', 'Schafer', 50000)
      self.emp_2 = Employee('Sue', 'Smith', 60000)
      
   def tearDown(self):
      pass

   # This will test to make sure that the email is automatically updated if the first name changes
   def test_email(self):
      emp_1.first = 'John'
      emp_2.first = 'Jane'

      self.assertEqual(emp_1.email, 'John.Schafer@email.com')
      self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

   # Test that full name changes when first or last name changes
   def test_fullname(self):
      # Test fullname functionality returns correctly
      self.assertEqual(emp_1.fullname, 'Corey Schafer')
      self.assertEqual(emp_2.fullname, 'Sue Smith')

      # Change a last name
      emp_1.last = "Smith"
      # Change a first name
      emp_2.first = "Jane"

      self.assertEqual(emp_1.fullname, 'Corey Smith')
      self.assertEqual(emp_2.fullname, 'Jane Smith')

if __name__ == '__main__':
   unittest.main()
