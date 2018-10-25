def tester1(x, L=[]):
    """Lista L rośnie po każdym wywołaniu funkcji."""
    L.append(x)
    print("tester1", L)

def tester2(x, L=None):
    """Lista L domyślnie zawsze pusta."""
    if L is None:
        L = []
    L.append(x)
    print("tester2", L)

tester1(1)
tester1(2)
tester1(3)
tester2(1)
tester2(2)
tester2(3)