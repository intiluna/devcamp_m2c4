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


# Exercise 4: Select the first element from your dictionary.
print("Exercise 4: Select the first element from your dictionary.")
print(mi_dict['name'])
print("------------------------------------")

# Exercise 5: Select the second element from your tuple.
print("Exercise 5: Select the second element from your tuple.")
print(mi_tuple[1])
print("------------------------------------")

# Exercise 6: Add an element to the end of your list.
print("Exercise 6: Add an element to the end of your list.")
mi_list.append("nuevo numero en la cola")
print(mi_list)
print("------------------------------------")

# Exercise 7: Replace the first element in your list.
print("Exercise 7: Replace the first element in your list.")
mi_list[0] = "101 days"
print(mi_list)
print("------------------------------------")

# Exercise 8: Sort your list alphabetically.
print("Exercise 8: Sort your list alphabetically.")

print(mi_list)
print("sort() no funciona con listas de distintos tipos de datos: TypeError: '<' not supported between instances of 'int' and 'str' asi que modificamos")
mi_list[0] = 18
mi_list[-1] = -15
print(f"lista modificada:\n{mi_list}")
mi_list.sort()
print(f"lista despues de sort:\n{mi_list}")
print("------------------------------------")


# Exercise 9: Use reassignment to add an element to your tuple.
print("Exercise 9: Use reassignment to add an element to your tuple.")
nuevo_elemento_para_tuple = ("more memory efficiente",)
print(f"nuevo elemento: {nuevo_elemento_para_tuple}")
mi_tuple += nuevo_elemento_para_tuple
print(mi_tuple)
print("------------------------------------")