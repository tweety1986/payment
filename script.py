waluta = "pln"
najem = input("Podaj kwotę najmu: ")
telefon_inernet = input("Podaj kwotę telefonu i internetu: ")
tv = input("Podaj kwotę za TV: ")
prad = input("Podaj kwotę za prąd: ")
woda = input("Podaj kwotę za wodę: ")
smieci = input("Podaj kwotę za smieci: ")
szambo = input("Podaj kwotę za szambo: ")
drewno = input("Podaj kwotę za drewno: ")
przedkole_dziecka_1 = input("Podaj kwotę za przedszkole dziecka_1: ")
przedszkole_dziecka_2 = input("Podaj kwotę za przedszkole dziecka_2: ")
lista_oplat = int(najem) + int(telefon_inernet) + int(tv) + int(prad) + int(woda) + int(smieci) + int(szambo) + int(drewno) + int(przedkole_dziecka_1) + int(przedszkole_dziecka_2)
zarobki_meza = input("Podaj zarobki meza: ")
zarobki_zony = input("Podaj zarobki zony: ")
dochody_razem = int(zarobki_meza) + int(zarobki_zony)
roznica = dochody_razem - lista_oplat

print("Lista Twoich opłat w tym miesiącu: ")
print("Kwota najmu to: " + najem + " " + waluta)
print("Kwota za internet i telefon: " + telefon_inernet + " " + waluta)
print("Kwota za TV: " + tv + " " + waluta)
print("Kwota za prąd: " + prad + " " + waluta)
print("Kwota za wodę: " + woda + " " + waluta)
print("Kwota za śmieci: " + smieci + " " + waluta)
print("Kwota za szambo: " + szambo + " " + waluta)
print("Kwota za drewno: " + drewno + " " + waluta)
print("Kwota za przedszkole dzieka_1: " + przedkole_dziecka_1 + " " + waluta)
print("Kwota za przedszkole dziecka_2: " + przedszkole_dziecka_2 + " " + waluta)
print("Opłaty razem: ", lista_oplat, waluta)
print("Nasze dochody: ", dochody_razem, waluta)
print("Zostanie: ", roznica, waluta)

def oplaty():
    if roznica > 0:
        print("Starczy!")
    else:
        print("Nie starczy!")
oplaty()

koszty_dojazdu_na_dzien = input("Podaj koszt paliwa na dzień: ")
ilosc_dni = input("Wpisz ilosc dni z dojazdem: ")
koszty_paliwa = int(koszty_dojazdu_na_dzien) * int(ilosc_dni)
print("Miesięczne koszty paliwa: ", koszty_paliwa, waluta)

koszty_wyzywienia_z_paragonów = input("Podaj kwoty z paragonów za zakupy: ")
koszty_leków = input("Podaj koszty leków: ")

kolejne_koszta = int(koszty_paliwa) + int(koszty_wyzywienia_z_paragonów) + int(koszty_leków)
print("Kolejne koszta:", kolejne_koszta, waluta)

def podsumowanie():
    if kolejne_koszta < roznica:
        print("Tez starczy!")
    else:
        print("Houston, mamy problem....")
podsumowanie()


reszta = roznica - kolejne_koszta
print("Zostanie jeszcze: ", reszta, waluta)

