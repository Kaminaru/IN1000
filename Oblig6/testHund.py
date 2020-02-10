from hund import Hund


def hovedprogram():
    """
    Prosedyre som oppretter hundeobjekt og kjorer flere test klassemetoder og printer vekt
    """
    hund1 = Hund(2,3)
    for i in range(5):
        print(hund1.hundVekt())
        hund1.spis(2)
        hund1.spis(1)
        hund1.spring()
        hund1.spring()
        print(hund1.hundVekt())

hovedprogram()
