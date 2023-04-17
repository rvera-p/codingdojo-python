if __name__ == '__main__':
    userName=input("Ingrese su nombre: ")
    age=int(input("Ingrese su edad: "))
    if age>20: 
        print(f'Yo {userName},soy un viejo y mi edad es {age}')
    elif age<=20: 
        print(f'Yo {userName}, soy joven y mi edad es {age}')