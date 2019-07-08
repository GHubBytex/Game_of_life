def spielfeldAusgeben(Spielfeld):
    for row in Spielfeld:
        for elem in row:
            print(elem, end=' ')
        print()


# Unsere hauptfunktion
def main():
    Spielfeld = [
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 0],
        ]
    spielfeldAusgeben(Spielfeld)

    for zeile in range(len(Spielfeld)):
        for spalte in range(len(Spielfeld[zeile])):
            aktuelleZelle = Spielfeld[zeile][spalte]
            anzahlLebenderNachbarn = 0

            # rechter nachbar
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 0][spalte + 1]
            # rechts unte
            if spalte + 1 < len(Spielfeld[zeile]) and zeile + 1 < len(Spielfeld):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 1][spalte + 1]
            if zeile + 1 < len(Spielfeld):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 1][spalte + 0]
            if zeile + 1 < len(Spielfeld) and spalte - 1 >= 0:
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 1][spalte - 1]
            if spalte - 1 >= 0:
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 0][spalte - 1]
            if spalte - 1 >= 0 and zeile -1 >= 0:
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile - 1][spalte - 1]
            if zeile - 1 >= 0:
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile - 1][spalte + 0]
            if spalte + 1 < len(Spielfeld[zeile]) and zeile - 1 >= 0:
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile - 1][spalte + 1]


            print('Lebende nachbarn von [' + str(zeile) + ',' + str(spalte) + ']:' + str(anzahlLebenderNachbarn))



if __name__ == '__main__':
    main()