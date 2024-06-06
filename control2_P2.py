nombres = []

print("Ingrese los nombres de las 7 personas")
for i in range(7):
    nombres.append(input(f"ingrese el nombre {i + 1}:"))
    
for nombre in nombres[:]:
    if nombre.endswith('a'):
        nombres.remove(nombre)

print("Los nombres de la lista despues de eliminar aquellos que terminan con 'a' son: ")
print(nombres)