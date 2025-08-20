# Declare int
x = 5

# Declare double
y = 3.14

# Declare boolean
flag = True

# ARRAYS:
# Create
nums = [1, 2, 3]
print("create:", nums)

# Length
length = len(nums)
print("length:", length)

# Access 
access = nums[0]
print("access:", access)

# Append
nums.append(4)
print("append:", nums)

# Slice
slice1 = nums[0:2]
print("slice:", slice1)


# HASHMAP / DICTIONARY
# create:
dictionary = {1: "Emi", 3: "Julieta"}
# any name
print("dictionary: ", dictionary)

# insert:
dictionary[2] = "José" # Entre corchetes es el key y lo que se le esta asignando = es el value
dictionary[4] = "Luis"
print(dictionary)

# lookup:
if 2 in dictionary: # Buscar si el key 2 esta en el dictionary para obtener su value
    print("It's value is: ", dictionary[2])

# LOOPS:
# for each
letters = ['a' , 'b', 'c']
for x in letters: # Usamos el array que definimos anteriormente
    print("for each", x)

# for each de index + value
for i, x in enumerate(letters): # enumerate genera pares: (indice, valor)
    print("Indice", i, "Valor", x)

# while
names = ["Juan", "Pedro", "Luis"]
i = 0
while i < len(names): 
    print(f"Indice {i}, Valor {names[i]}") # f le dice a python, lo que esta entre llaves dentro del texto se reemplaza por el valor de la variable.
    i+=1

# return
# return [i, j]

# CLASSES 
class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola! mi nombre es {self.nombre} y mi edad es {self.edad}")

p1 = Persona("Emi", 20)

p1.saludar()

# SETS:
# coleccion desordenada sin elementos repetidos
sets = {"manzana", "pera", "manzana", "uva"}
print(sets)
sets.add("platano")
print("despues de agregar platano: ", sets)
sets.remove("pera")
print("despues de eliminar pera", sets)

# definir funciones
def two_sum(self, nums, target):
    # nuestro codigo 
    return [nums, target] # regresa lista con dos elementos


# STRINGS:
nombre = "Emiliano"
print(f"Nombre: {nombre}")

# length:
length_name = len(nombre)
print(f"tamaño del nombre {nombre}: {length_name}")

# obtener char en:
char = nombre[2]
print("char en 2: ", char)

# substring:
substring_nombre = nombre[1:3]
print("substring: ", substring_nombre)



