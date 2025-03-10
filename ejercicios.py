# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
print("Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.")
# List
mi_list = [1, 2, 3, 4, 5]
print(mi_list)

# Tuple
mi_tuple = ("important", "danger", "not try to change", "immutable")
print(mi_tuple) 

# Float
mi_float = 41.2
print(mi_float)

# Integer
mi_integer = 41
print

# Decimal
from decimal import Decimal
mi_decimal = Decimal('41.2')
print(mi_decimal)

# Dictionary
mi_dict = {'name': 'Kathy', 'age': 5, 'city': 'Managua'}
print(mi_dict)
print("------------------------------------")


# Exercise 2: Round your float up.
print("Exercise 2: Round your float up.")

import math

mi_nuevo_float = math.ceil(mi_float)
print(mi_nuevo_float)
print("------------------------------------")

#Exercise 3: Get the square root of your float.
print("Exercise 3: Get the square root of your float.")
mi_square_root = math.sqrt(mi_float)
print(mi_square_root)
print("------------------------------------")
