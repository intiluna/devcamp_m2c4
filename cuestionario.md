# Cuestionario Checkpoint 4
Inti Luna
2025-03-10

## ¿Cuál es la diferencia entre una lista y una tupla en Python?

- Listas se definen con \[\] y tuplas con ().
- Listas son modificables y tuplas no.
- Listas tiene una cantidad de elementos dinámicas y tuplas no, estas
  son fijas (por son inmutables).
- Procesos con listas son más lentos que con tuplas.
- Las listas son menos eficientes en términos de memoria que las tuplas.

``` python
lista = [1,2,3,4]
print(lista)
lista[3]="perro"
lista.append(["una","nested","lista"])
print(lista)
print(f"elementos en lista:{len(lista)}")
mi_tupla = (1,2,3)
print(mi_tupla)
print(f"elementos en tupla:{len(mi_tupla)}")
```

    [1, 2, 3, 4]
    [1, 2, 3, 'perro', ['una', 'nested', 'lista']]
    elementos en lista:5
    (1, 2, 3)
    elementos en tupla:3

Referencias
<https://builtin.com/software-engineering-perspectives/python-tuples-vs-lists>.

## ¿Cuál es el orden de las operaciones?

Según PEMDAS el orden es: P -\> Parantesis () E -\> Exponentes \*\* M
-\> Multiplicacion \* D -\> Division / A -\> Addition o suma + S -\>
Subtraction o resta - Se puede intercambiar el orden de multiplicación y
división y el resultado sería el mismo.

``` python
resultado = 5 + (5-2) + 3*2 + 2**2
print(f"resultado:{resultado}")
```

    resultado:18

## ¿Qué es un diccionario Python?

Es una estructura de almacenamiento o colección de datos en python que
se basa en llaves y valores (key:values) que es muy usada para almacenar
información diferente y es muy utilizada. Es muy similar a JSON
(JavaScript Object Notation) que es un protocolo estándar para
comunicaciones para interactuar con API(Application Programming
Interfaces)s.

``` python
sat_data = {'cloudy_pixel_percentage':0.8, 'id':'20220225_AXC', 'country':'Ecuador', 'satellite':'sentinel-2'}

# adding elemento to dictionary
print("add item:")
sat_data["land_cover"]="forest"
print(sat_data)

#operaciones
print("get item operation:")
sat_data.get("river", "not available") 
sat_data.get("id")

# to view but not index
print(f"keys:\n{sat_data.keys()}")
print(f"values:\n{sat_data.values()}")
print(f"items:\n{sat_data.items()}")

# to index
print("index item:")
print(list(sat_data.keys())[1])
print(list(sat_data.values())[2])

print("delete item:")
# to delete (safely)
default_delete = "Item not found for removing"
removed_item = sat_data.pop("speed", default_delete)
removed_item2 = sat_data.pop("cloudy_pixel_percentage", default_delete)
print(removed_item)
print(removed_item2)
print(sat_data)
```

    add item:
    {'cloudy_pixel_percentage': 0.8, 'id': '20220225_AXC', 'country': 'Ecuador', 'satellite': 'sentinel-2', 'land_cover': 'forest'}
    get item operation:
    keys:
    dict_keys(['cloudy_pixel_percentage', 'id', 'country', 'satellite', 'land_cover'])
    values:
    dict_values([0.8, '20220225_AXC', 'Ecuador', 'sentinel-2', 'forest'])
    items:
    dict_items([('cloudy_pixel_percentage', 0.8), ('id', '20220225_AXC'), ('country', 'Ecuador'), ('satellite', 'sentinel-2'), ('land_cover', 'forest')])
    index item:
    id
    Ecuador
    delete item:
    Item not found for removing
    0.8
    {'id': '20220225_AXC', 'country': 'Ecuador', 'satellite': 'sentinel-2', 'land_cover': 'forest'}

Referencias:
<https://heardlibrary.github.io/digital-scholarship/script/python/json/>

## ¿Cuál es la diferencia entre el método ordenado y la función de ordenación?

El método sort() ordena una lista por orden alfabético o por orden de
valor, afectando la lista original pero no regresa (return) nada. En
cambio la función sorted() regresa la lista ordenada y no afecta a la
lista original.

``` python
lista_a = [6,5,3,8,89,12,1]
lista_b = lista_a.copy()

# usando sort()
print(f"lista antes de usar sort():\n{lista_a}")
lista_a.sort(reverse=True)
print(f"lista a despues de usar sort():\n{lista_a}")

# usando sorted()
print(f"lista antes de usar sorted():\n{lista_b}")
lista_c = sorted(lista_b)
print(f"lista despues de usar sorted():\n{lista_b}")
print(f"lista c:\n{lista_c}")
```

    lista antes de usar sort():
    [6, 5, 3, 8, 89, 12, 1]
    lista a despues de usar sort():
    [89, 12, 8, 6, 5, 3, 1]
    lista antes de usar sorted():
    [6, 5, 3, 8, 89, 12, 1]
    lista despues de usar sorted():
    [6, 5, 3, 8, 89, 12, 1]
    lista c:
    [1, 3, 5, 6, 8, 12, 89]

## ¿Qué es un operador de reasignación?

La asignación es cuando establecemos que una variable apunta a una
expresión o valor. En la reasignación como el nombre indica indicamos
otro valor o expresión a la misma variable.

``` python
#asigamos valores a lista_a
lista_a = [6,5,3,8,89,12,1]
print(lista_a)

#reasignamos
lista_a = 101
print(f"nuevo valor en misma variable:\n{lista_a}")

lista_a += 10
print(f"nuevo valor en misma variable:\n{lista_a}")

lista_a -= 100
print(f"nuevo valor en misma variable:\n{lista_a}")

lista_a *= 10
print(f"nuevo valor en misma variable:\n{lista_a}")
```

    [6, 5, 3, 8, 89, 12, 1]
    nuevo valor en misma variable:
    101
    nuevo valor en misma variable:
    111
    nuevo valor en misma variable:
    11
    nuevo valor en misma variable:
    110

Referencias:

<https://www.w3schools.com/python/gloss_python_assignment_operators.asp>

<https://realpython.com/python-assignment-operator/>
