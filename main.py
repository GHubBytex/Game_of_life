import time
import random
import sys
def spielfeldAusgeben(Spielfeld):
    for Zeile in Spielfeld:
        for Zelle in Zeile:
            if Zelle == 0:
                print(" ", end=' ')
            else: 
                print("O", end=' ')
        print()
    time.sleep(0.2)
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


    #print('Lebende nachbarn von [' + str(zeile) + ',' + str(spalte) + ']:' + str(anzahl))
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
    print('Number of arguments: ' + str(len(sys.argv)) + ' arguments.')
    print('Argument List:' + str(sys.argv))
    time.sleep(0.6)
    print("*********************")
    print("Spiel startet in 3 Sekunden!")
    time.sleep(1)
    print("Bitte Warten")
    time.sleep(3)

    Spielfeld = [[0 for i in range(50)] for j in range(50)]


    for zeile in range(len(Spielfeld)):
        for spalte in range(len(Spielfeld[zeile])):
            x = random.randint(0,1)
            Spielfeld[zeile][spalte] = x

    spielfeldAusgeben(Spielfeld)

    # Dies wiederholen:
    while nochEtwasLebtIm(Spielfeld):
        Folgegeneration = [[0 for i in range(50)] for j in range(50)]

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

if __name__ == '__main__':
    main()





117
53


