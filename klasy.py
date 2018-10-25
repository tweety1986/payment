class Rachunki:
  def __init__(self, oplata, kwota):
    self.oplata = oplata
    self.kwota = kwota

p1 = Rachunki(input("nazwa:"), input('kwota:'))

print(p1.oplata)
print(p1.kwota)

