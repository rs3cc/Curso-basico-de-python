# 1 dolar Mexico = 19.88 
# 1 dolar Argentina = 124
# 1 dolar Colombia = 4198.77
# 1 peso a dolar Mexico = 0.049304122
# 1 peso a dolar Argentina = 0.0079710943
# 1 peso a dolar Colombia = 0.00023781003

def conversor(valor_peso):
    dolares = int(input("Cuantos dolares tienes? "))
    pesos = dolares / valor_peso
    pesos = round(pesos, 2)
    print("Tienes $" + str(pesos) + " pesos")

menu = """ 
        BIENVENIDO AL CONVERSOR DE DOLARES A PESOS
                    
                    1 - Pesos Mexicanos
                    2 - Pesos Argentinos
                    3 - Pesos Colombianos

ELIGE UNA OPCION: """

opcion = int(input(menu))

if opcion == 1:
    conversor(0.049304122)
elif opcion == 2:
    conversor(0.0079710943)
elif opcion == 3:
    conversor(0.00023781003)
else:
    print("Elige una opcion correcta")