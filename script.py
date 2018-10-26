def lista_platnosci():
    lista_platnosci = []
    while True:
        platnosc = input('Płatność za: ')
        lista_platnosci.append(platnosc)
        if platnosc == 'stop':
            break
        print(lista_platnosci)
lista_platnosci()











