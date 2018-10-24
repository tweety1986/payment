def lista_uslug():
    lista_uslug = []
    x = int(input('Podaj, ile usług chcesz dodać?'))
    for koszta in range(x):
        x = input("Podaj, nazwę usługi:")
        lista_uslug.append(x)
    return lista_uslug


def input_type(lista_uslug):
    wynik = 0
    waluta = 'PLN'
    lista_output = []
    for wydatki in lista_uslug:
        x = input('Podaj kwotę za {}:'.format(wydatki))
        lista_output.append(x)
    for i in lista_output:
        wynik = wynik + int(i)
    print ("Opłaty razem: ", wynik, waluta)
input_type(lista_uslug())

def lista_przychody():
    lista_przychody = []
    x = int(input('Podaj, ile żródeł dochodu posiadasz?'))
    for pensja in range(x):
        x = input("Czyj to dochód?")
        lista_przychody.append(x)
    return lista_przychody

def input_type(lista_przychody):
    wynik2 = 0
    waluta = 'PLN'
    lista_output = []
    for pensja in lista_przychody:
        x = input('Podaj kwotę przychodu {}:'.format(pensja))
        lista_output.append(x)
    for i in lista_output:
        wynik2 = wynik2 + int(i)
    print ("Przychody razem: ", wynik2, waluta)
    def zestawienie():
        if wynik2 < 6200:
            print('Powinno starczyc.')
        else:
            print('Raczej nie starczy.')
    zestawienie()

input_type(lista_przychody())

