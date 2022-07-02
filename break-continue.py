# def run():
#     for i in range(10000):
#         if i == 6667:
#             break
#         print(i)


# if __name__ == "__main__":
#     run()

# def run():
#     texto = input("Escribe un texto: ")
#     for i in texto:
#         if i == "o":
#             break
#         print(i)


# if __name__ == "__main__":
#     run()

# def run():
#     for contador in range(1000):
#         if contador % 2 != 0:
#             continue
#         print(contador)


# if __name__ == "__main__":
#     run()
menu = """
Bienvenido al juego de adivinar letras:

Adivina la letra para ganar: Solo tienes 5 intentos para adivinar la letra secreta:

Escribe A para comenzar: """


def run():
    iniciar = input(menu)
    intentos = 0
    if iniciar != "A":
        print("Escribe la opcion correcta")
    if iniciar == "A":
            while intentos < 5:
                letra = input("Cual es la letra secreta? ")
                letra = letra.lower()
                intentos = intentos + 1
                if letra == "r":
                    print("Ganaste, la letra secreta es R")
                    break
                if intentos == 5:
                    print("Perdiste, intentalo de nuevo")
    

if __name__ == "__main__":
    run()














