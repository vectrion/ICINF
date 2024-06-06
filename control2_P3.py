palabras = []

while True:
    palabra = input("Ingrese una palabra (presione Enter para terminar): ")
    if palabra == "":
        break
    palabras.append(palabra)
     
if palabras:
    menor_longitud = len(palabras[0])
    for palabra in palabras:
        if len(palabra) < menor_longitud:
            menor_longitud = len(palabra)
print("la palabra que tiene menos caracteres tiene",menor_longitud, "caracter(es) ")