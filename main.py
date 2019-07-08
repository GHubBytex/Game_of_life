import time
def spielfeldAusgeben(Spielfeld):
    for row in Spielfeld:
        for elem in row:
            print(elem, end=' ')
        print()
    time.sleep(1)  
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


# Unsere hauptfunktion
def main():
    Spielfeld = [
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 0],
        ]
    Folgegeneration = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        ]
    spielfeldAusgeben(Spielfeld)

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







if __name__ == '__main__':
    main()