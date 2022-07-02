def conversor(pais, valor):
    pesos = int(input("Cuantos pesos " + pais + " tienes? "))
    valor_dolar = valor
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " dolares")


menu = """
BIENVENIDO AL CONVERSOR DE PESOS A DOLARES:

1 - Pesos Mexicanos
2 - Pesos Argentinos
3 - Pesos Colombianos

ELIGE UNA OPCION: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Mexicanos", 19.88)
elif opcion == 2:
    conversor("Argentinos", 57)
elif opcion == 3:
    conversor("Colombianos", 3560)
else:
    for er in str("Elige una opcion correcta"):
        print(er.upper())