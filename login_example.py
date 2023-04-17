if __name__ == '__main__':
    psswd1 = "UserPassword" 
    while True:
        psswd2 = input("Ingrese su contraseña: ")
        if psswd1.upper() == psswd2.upper(): 
            print("Bienvenido usuario!")
            break
        else: print("Contraseña erronea, por favor intentar de nuevo.")