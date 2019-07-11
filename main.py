import time
import random
import sys

def spielfeldAusgeben(Spielfeld):
    for Zeile in Spielfeld:
        for Zelle in Zeile:
            if Zelle == 0:
                print(" ", end=' ')
            else:
                print("*", end=' ')
        print()
    time.sleep(0.6)
    print()

def zähle_die_nachbarn(Spielfeld, zeile, spalte):
    anzahl = 0
    if spalte + 1 < len(Spielfeld[zeile]):
        anzahl = anzahl + Spielfeld[zeile + 0][spalte + 1]
    if spalte + 1 < len(Spielfeld[zeile]) and zeile + 1 < len(Spielfeld):
        anzahl = anzahl + Spielfeld[zeile + 1][spalte + 1]
    if zeile + 1 < len(Spielfeld):
        anzahl = anzahl + Spielfeld[zeile + 1][spalte + 0]
    if zeile + 1 < len(Spielfeld) and spalte - 1 >= 0:
        anzahl = anzahl + Spielfeld[zeile + 1][spalte - 1]
    if spalte - 1 >= 0:
        anzahl = anzahl + Spielfeld[zeile + 0][spalte - 1]
    if spalte - 1 >= 0 and zeile -1 >= 0:
        anzahl = anzahl + Spielfeld[zeile - 1][spalte - 1]
    if zeile - 1 >= 0:
        anzahl = anzahl + Spielfeld[zeile - 1][spalte + 0]
    if spalte + 1 < len(Spielfeld[zeile]) and zeile - 1 >= 0:
        anzahl = anzahl + Spielfeld[zeile - 1][spalte + 1]

    return anzahl

def nochEtwasLebtIm(Spielfeld):
    for zeile in Spielfeld:
        for zelle in zeile:
            if zelle == 1:
                return True
    # Alles tot!
    return False

# Unsere hauptfunktion
def main():
    time.sleep(0.4)
    print("****************************")
    print("Spiel startet in 2 Sekunden!")
    print("Bitte Warten")
    time.sleep(2)
    print("****************************")

    anzahl_lebendig_zellen = int(input("Wie viele Zellen sollen lebendig sein? "))
    größe = int(input("Wie groß soll das Spielfeld sein? "))

    größe_im_quadrat = größe * größe
    if größe_im_quadrat <= anzahl_lebendig_zellen:
        Fehlermeldung_zu_viel_Zellen()
        exit()



    Spielfeld = [[0 for i in range(größe)] for j in range(größe)]

    Zufallsgenerator(Spielfeld, anzahl_lebendig_zellen, größe)

    spielfeldAusgeben(Spielfeld)

    while nochEtwasLebtIm(Spielfeld):
        Folgegeneration = [[0 for i in range(größe)] for j in range(größe)]

        for zeile in range(len(Spielfeld)):
            for spalte in range(len(Spielfeld[zeile])):
                anzahl = zähle_die_nachbarn(Spielfeld, zeile, spalte)
                if anzahl == 3:
                    Folgegeneration[zeile][spalte] = 1
                if anzahl < 2:
                    Folgegeneration[zeile][spalte] = 0
                if Spielfeld[zeile][spalte] == 1:
                    if anzahl == 3 or anzahl == 2:
                        Folgegeneration[zeile][spalte] = 1
                    if anzahl > 3:
                        Folgegeneration[zeile][spalte] = 0

        spielfeldAusgeben(Folgegeneration)
        Spielfeld = Folgegeneration
    # bis hierher

def Zufallsgenerator(Spielfeld, anzahl_lebendig_zellen, größe):
    i = 0
    while i < anzahl_lebendig_zellen:
        zeile = random.randint(0,größe - 1)
        spalte = random.randint(0,größe - 1)
        if Spielfeld[zeile][spalte] == 0:
            i += 1
            Spielfeld[zeile][spalte] = 1

def Fehlermeldung_zu_viel_Zellen():
    print("Sie haben zu viele lebende Zellen! ")
    print("Spiel schließt")



if __name__ == '__main__':
    main()
