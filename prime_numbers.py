with open("prime_numbers.txt", "w") as f: #Creamos el archivo txt
    for n in range (1, 250, 1): #Recorremos los numeros del 1 al 250
        prime = True    #Primo por defecto
        for i in range(2, n, 1):
            if(n%i == 0): #Si el numero es divisible por el numero i y es igual 0 "prime" no es primo y lo salta
                prime = False
                break
        if (prime == True and n!=1):
            f.write(str(n) + "\n") #Escribe en el archivo con salto de linea