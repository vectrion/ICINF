capitales_paises = {}
print("ingrese 5 paises y 5 capitales")
for i in range(5):
    capital = input("ingrese una capital: ")
    pais = input("ingrese el pais al que pertenece esa capital: ")
    capitales_paises[capital] = pais

print("capitales (y su respectivo pais) ingresados: ")
print(capitales_paises)

nombre_turista = input("cual es el nombre del turista? ")
capital_turista = input("cual es la capital del pais de origen del turista? ")

pais_turista = "desconocido"

if capital_turista in capitales_paises:
    pais_turista = capitales_paises[capital_turista]
print("el turista con el nombre " + nombre_turista + " viene de la capital " + capital_turista + " y su pais es " + pais_turista)