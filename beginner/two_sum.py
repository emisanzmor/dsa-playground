# TWO SUM: Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# EXPLICACIÓN:
# Imagina que tienes un array o lista de números y un número objetivo.
# Necesitas encontrar dos números de la lista que al sumarse den el número objetivo (TARGET).
 
# No queremos los números, queremos las posiciones de la lista.
class TwoSum:
     # nums: lista de números / target: el número objetivo
    def two_sum(self, nums, target):
    # Diccionario para recordar números que ya vimos
        seen = {}

    # Recorro cada número con su posición
        for i, num in enumerate(nums):
        # En cada uno se realiza la siguiente operación
            complement = target - num

        # Ya se vió el número antes? (Ya está en el diccionario seen? )
            if complement in seen:

            # Retornamos una lista con las dos posiciones
                return [seen[complement], i] # Se retorna la posición donde está el complemento en seen y la posicion del num que se estaba evaluando.

            # Si no estaba complement en seen, se agregan el num y su posición al diccionario.s
            seen[num] = i

        return []


two_sum1 = TwoSum()
print(two_sum1.two_sum([3, 3], 6)) # Se le da un array de numeros y el target. Debe de retornar [0, 1]
print(two_sum1.two_sum([1,2,3,4,5], 9)) # Debe de retornar [3, 4]

# EXPLICACIÓN:
# El problema nos da un array de enteros y un número objetivo (target). Tenemos que devolver los índices de dos números cuya suma dé exactamente el target.
# En la clase TwoSum definimos el método two_sum, que recibe la lista de números y el target.
# Creamos un diccionario seen que servirá para ir guardando cada número que veamos como clave y su índice como valor.
# Recorremos la lista con enumerate para obtener en cada vuelta tanto el índice como el número. En cada iteración calculamos el complemento: target - num.
# Si ese complemento ya está en el diccionario, significa que en un ciclo anterior ya vimos el número que falta para formar el target. Entonces devolvemos una lista con dos índices: el del complemento (seen[complement]) y el del número actual (i).
# Si el complemento no estaba, guardamos el número actual en el diccionario para usarlo en vueltas futuras: seen[num] = i.
# Si terminamos todo el bucle sin encontrar solución, devolvemos una lista vacía [].



