# Given a string s, return the index of the first non repeating character in it.
# if it does not exists, return -1.

def first_unique_char(s: str) -> int:
    char_count = {} # Diccionario que guarda cada caracter como key y la cantidad de veces que aparece como valor. 

     # Contamos cada letra en la palabra y la guardamos en el diccionario la letra como key y la cantidad de veces que existe en la palabra como value.
    for char in s: # Iterate through each char of the word one by one
        char_count[char] = char_count.get(char, 0) + 1  # Busca si la letra / clave char de la iteración actual ya existe en el diccionario, si no existe aún devuelve 0.
        # El +1 incrementa el conteo del char en el diccionario porque lo acabamos de ver.
        # Se actualiza en el diccionario la cantidad de veces vista la letra en "char_count[char]"

    # Buscamos el primer char único / que no se repite
    for i, char in enumerate(s): # iteramos obteniendo cada char y su index de la palabra.
        if char_count[char] == 1: # Se evalua en cada iteración, se busca el char iterado en el diccionario y la primera letra que tenga value 1 retorna su index.
            return i


    return -1 # Si ninguna key o letra fue unica, se retorna -1.

# Test cases

print(first_unique_char("leetcode"))    # Expected 0
print(first_unique_char("loveleetcode")) # Expected 2
print(first_unique_char("aabb"))        # Expected -1
print(first_unique_char(""))            # Expected -1

# Complexity O(n) because I make two passes over the string, and space complexity O(1) since the alphabet is fixed.
