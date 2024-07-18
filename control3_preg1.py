def digitos(num):
    num_str=str(num)
    cantidad_digitos=len(num_str)
    return cantidad_digitos
    
numero=input("ingresar un numero:")

try:
    numero=int(numero)
    print("el numero", numero, "tiene", digitos(numero), "digitos")

except ValueError:
    print("ingrese un numero valido por favor")