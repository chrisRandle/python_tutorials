
def add(x, y):
   """Add Function"""
   return x + y

def subtract(x, y):
   """Subtract Function"""
   return x - y

def multiply(x, y):
   """Multiply Function"""
   return x * y

def divide(x, y):
   """Divide Function"""
   if y == 0:
      raise ValueError('Can not divide by zero.')
   return x / y

def floor_divide(x, y):
   # Floor division returns only whole numbers
   if y == 0:
      raise ValueError('Can not floor divide by zero.')
   return x // y

