import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

   # This will test to make sure that the email is automatically updated if the first name changes
   def test_email(self):
      # Set employee first, last, salary
      emp_1 = Employee('Corey', 'Schafer', 50000)
      emp_2 = Employee('Sue', 'Smith', 60000)

      self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
      self.assertEqual(emp_2.email, 'Sue.Smith@email.com')

      emp_1.first = 'John'
      emp_2.first = 'Jane'

      self.assertEqual(emp_1.email, 'John.Schafer@email.com')
      self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

   # Test that full name changes when first or last name changes
   def test_fullname(self):
      # Set employee first, last, salary
      emp_1 = Employee('Corey', 'Schafer', 50000)
      emp_2 = Employee('Sue', 'Smith', 60000)

      self.assertEqual(emp_1.fullname, 'Corey Schafer')
      self.assertEqual(emp_2.fullname, 'Sue Smith')

      emp_1.last = "Smith"
      emp_2.first = "Jane"

      self.assertEqual(emp_1.fullname, 'Corey Smith')
      self.assertEqual(emp_2.fullname, 'Jane Smith')

if __name__ == '__main__':
   unittest.main()
