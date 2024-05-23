# Leer el total de preguntas
total_preguntas = int(input("Ingrese el total de preguntas: "))

# Leer la cantidad de respuestas correctas
respuestas_correctas = int(input("Ingrese la cantidad de respuestas correctas: "))

# Calcular el porcentaje de respuestas correctas
porcentaje = (respuestas_correctas / total_preguntas) * 100

# Determinar el nivel según el porcentaje
if porcentaje >= 95:
    nivel = "Nivel máximo"
elif porcentaje >= 70:
    nivel = "Nivel medio"
elif porcentaje >= 40:
    nivel = "Nivel regular"
else:
    nivel = "Fuera de nivel"

# Imprimir el resultado
print(f"El porcentaje de respuestas correctas es: {porcentaje:.2f}%")
print(f"El nivel del postulante es: {nivel}")