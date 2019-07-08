def spielfeldAusgeben(Spielfeld):
    for row in Spielfeld:
        for elem in row:
            print(elem, end=' ')
        print()


# Unsere hauptfunktion
def main():
    Spielfeld = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        ]
    spielfeldAusgeben(Spielfeld)

    for zeile in range(len(Spielfeld)):
        for spalte in range(len(Spielfeld[zeile])):
            aktuelleZelle = Spielfeld[zeile][spalte]
            anzahlLebenderNachbarn = 0
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 0][spalte + 1]
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 1][spalte + 1]
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 1][spalte + 0]
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 1][spalte - 1]
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile + 0][spalte - 1]
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile - 1][spalte - 1]
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile - 1][spalte + 0]
            if spalte + 1 < len(Spielfeld[zeile]):
                anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[zeile - 1][spalte + 1]






            anzahlLebenderNachbarn = anzahlLebenderNachbarn + Spielfeld[1][0]
            print('Lebende nachbarn von [' + str(zeile) + ',' + str(spalte) + ']:' + str(anzahlLebenderNachbarn))



if __name__ == '__main__':
    main()

