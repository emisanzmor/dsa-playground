# Procesar lista de usuarios en JSON:

usuarios = [
    {"nombre": "Ana", "edad": 25, "departamento": "IT"},
    {"nombre": "Carlos", "edad": 30, "departamento": "Marketing"},
    {"nombre": "Diana", "edad": 28, "departamento": "IT"},
    {"nombre": "Eduardo", "edad": 35, "departamento": "Ventas"}
]

# 1. Filtra solo usuarios de IT
# 2. Crea un diccionario con nombre como key y edad como value
# 3. Encuentra la edad promedio de usuarios de IT

usuarios_it = [usuario for usuario in usuarios if usuario["departamento"] == "IT"] # Recorre la lista que cada elemento es un diccionario {} en busca de que el key "departamento" incluya el value "IT"
nombres_edades = {usuario["nombre"]: usuario["edad"] for usuario in usuarios_it} # Vamos a recorrer en la lista de usuarios IT y crear un diccionario con esos datos para filtrar solo por departamento IT.

# EXTRA: SACAR EL PROMEDIO DE EDAD DE LOS USUARIOS CON DEPARTAMENTO IT:
total_edad = sum(usuario["edad"] for usuario in usuarios_it)
promedio = total_edad / len(usuarios_it)

print(usuarios_it) # [{'nombre': 'Ana', 'edad': 25, 'departamento': 'IT'}, {'nombre': 'Diana', 'edad': 28, 'departamento': 'IT'}]
print(nombres_edades) # {'Ana': 25, 'Diana': 28}
print(total_edad) # 53
print(promedio) # 26.5

# PRACTICA
# Procesar lista de usuarios en JSON:

usuarios = [
    {"nombre": "Ana", "edad": 25, "departamento": "IT"},
    {"nombre": "Carlos", "edad": 30, "departamento": "Marketing"},
    {"nombre": "Diana", "edad": 28, "departamento": "IT"},
    {"nombre": "Eduardo", "edad": 35, "departamento": "Ventas"}
]

# 1. Filtra solo usuarios de IT
# 2. Crea un diccionario con nombre como key y edad como value
# 3. Encuentra la edad promedio de usuarios de IT

usuarios_it = [usuario for usuario in usuarios if usuario["departamento"] == "IT"]
personas_edad = {usuario["nombre"]: usuario["edad"] for usuario in usuarios_it}

# Promedio:

usuarios_sum = sum(usuario["edad"] for usuario in usuarios_it)
usuario_promedio = usuarios_sum / len(usuarios_it)

print(personas_edad)
print(usuarios_sum)
print(usuario_promedio)
usuarios

