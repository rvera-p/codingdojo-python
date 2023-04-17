#Generador de Password
#Debe permitir cuantos caracteres tiene
#Mayusculas y Minusculas por defecto
#Caracteres especiales y numeros opcional
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

    get_random_string(5)
    get_random_string(3)