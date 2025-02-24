def encriptar(texto,clave):
    texto_encriptado = ""
    for letra in texto:
        if letra != " ":
            caracter = chr(ord(letra) + clave)
            texto_encriptado += caracter
        else:
            texto_encriptado += " "
    return texto_encriptado

def desencriptar(texto,clave):
    texto_desencriptado = ""
    for letra in texto:
        if letra != " ":
            caracter = chr(ord(letra) - clave)
            texto_desencriptado += caracter
        else:
            texto_desencriptado += " "
    return texto_desencriptado

print(encriptar(input("Escriba un texto: "),int(input("Escriba un numero: "))))
print(desencriptar(input("Escriba un texto: "),int(input("Escriba un numero: "))))