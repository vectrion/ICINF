puntajes = []

print("Ingrese los puntajes diarios del alumno (de 1 a 100) para los 15 días de curso:")
for dia in range(1, 16):
    puntaje = int(input(f"Puntaje del día {dia}: "))
    puntajes.append(puntaje)

print("\nDías con puntaje menor a 70 puntos:")
for dia in range(15):
    if puntajes[dia] < 70:
        print(f"Día {dia + 1}")
        
print("\nDías con puntaje igual o mayor a 70 puntos:")
for dia in range(15):
    if puntajes[dia] >= 70:
        print(f"Día {dia + 1}")