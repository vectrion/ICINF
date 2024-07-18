def potencia(num, exp):
  
    if exp == 0:
        return 1
    
    else:
         return num * potencia(num, exp - 1)

numero = int(input("ingrese un numero base:"))
exponente = int(input("ingrese el exponente para el numero base:"))

resultado = potencia(numero, exponente)
print("el resultado de", numero, "elevado a", exponente, "es", resultado)