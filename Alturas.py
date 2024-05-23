alturas = []

print("Ingrese las alturas en metros (para terminar, ingrese 0):")

while True:
    
    altura = float(input("Altura: "))

    if altura == 0:
        break
    
    alturas.append(altura)

if len(alturas) > 0:
    promedio = sum(alturas) / len(alturas)
    print(f"La altura promedio es: {promedio:.2f} metros")
else:
    print("No se ingresaron alturas.")