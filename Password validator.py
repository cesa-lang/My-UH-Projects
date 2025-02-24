while True:
    password = input("Ingrese una contrasena: ")
    if len(password) > 6:
        if len([x.isdigit() for x in password]) > 0:
            if any(x.isupper() for x in password):
                print("Es valida")
                break
    
    print("Es invalida")