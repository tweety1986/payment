def lista_platnosci():
    lista_platnosci = []
    while True:
        platnosc = input('Płatność za: ')
        x = input('kwota:')
        lista_platnosci.append(platnosc)
        lista_platnosci.append(x)
        if platnosc == 'stop':
            break

        print(lista_platnosci)

lista_platnosci()

def lista_wynikow(lista_platnosci):
    lista_wynikow = []
    for x in range(lista_platnosci):
        print(int(x))
lista_wynikow()














