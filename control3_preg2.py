def es_binario(var):
    for char in var:
        if char != '0' and char != '1':
            return False
    return True

cadena = input("ingrese una cadena:")

if es_binario(cadena):
    print("la cadena", cadena, "es una expresion binaria")
else:
    print("la cadena", cadena, "no es una expresion binaria")