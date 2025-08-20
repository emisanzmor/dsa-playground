# PRACTICA:

# Given a string s, return True if it is a palindrome, and False otherwise.
# A palindrome is a word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and capitalization.

# Example: 
# Input: "A man, a plan, a canal: Panama"
# Output: True
# Explanation: After removing non-alphanumeric characters and ignoring cases, it becomes "amanaplanacanalpanama" which is palindrome.

# Input: "race a car"
# Output: False
# Explanation: After processing, it becomes "raceacar" which is not the same backward.


def is_palindrome(s: str) -> bool:  # Definimos la función "is_palindrome" con parametro s de tipo string, la función debe de retornar un bool.
    left = 0 # Primer puntero, empieza al inicio del string dado.
    right = len(s) - 1 # Segundo puntero, empieza al final del string. Como los indices empiezan en 0, el ultimo indice debe de ser length - 1

    while left < right:  # Mientras no se crucen los punteros 

        while left < right and not s[left].isalnum(): # Mientras no se crucen los punteros y el char en el indice left sea un espacio o puntuacion, left avanza 1. 
            left += 1

        while left < right and not s[right].isalnum(): # Mientras no se crucen los punteros y el char en el indice right sea un espacio o puntuacion, right avanza 1. 
            right -= 1

        if s[left].lower() != s[right].lower():  # Si el char en left y el char en right son diferentes, entonces no es palindromo y devuelve false. La comparacion se hace con los char en minuscula.
            return False

        left += 1 # Puntero left avanza 1
        right -= 1 # Puntero right retrocede 1
        
    return True


print(is_palindrome("A car"))
print(is_palindrome("A man, a plan, a canal: Panama"))
        









