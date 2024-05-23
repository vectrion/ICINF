entre_500k_y_900k = 0
mas_de_900k = 0
gasto_total = 0

while True:
    sueldo = float(input("Ingrese el sueldo del empleado (ingrese -1 para finalizar): "))
    if sueldo == -1:
        break
    if 500000 <= sueldo <= 1500000:
        gasto_total += sueldo
        if sueldo <= 900000:
            entre_500k_y_900k += 1
        else:
            mas_de_900k += 1
    else:
        print("El sueldo ingresado no está en el rango permitido (500.000 a 1.500.000). Intente de nuevo.")

# Mostrar los resultados
print(f"Cantidad de empleados que cobran entre $500.000 y $900.000: {entre_500k_y_900k}")
print(f"Cantidad de empleados que cobran más de $900.000: {mas_de_900k}")
print(f"El gasto total en sueldos es: ${gasto_total:,.2f}")