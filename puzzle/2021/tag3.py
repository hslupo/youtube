

def read_puzzle(file):
  with open(file) as f:
      return [zeile.strip() for zeile in f]

def solve(puzzle):
    spalten = len(puzzle[0])
    zeilen = len(puzzle)
    erg = ''
    inv = ''

    for spalte in range(spalten):
        zeilenzahl = 0
        zeilen_0 = []
        zeilen_1 = []
        for zeile in range(zeilen):
            if puzzle[zeile][spalte] == '1':
                zeilenzahl += 1
                zeilen_1.append(puzzle[zeile])
            else:
                zeilen_0.append(puzzle[zeile])
            # print(spalte, zeile, puzzle[zeile], puzzle[zeile][spalte], zeilenzahl)
            print(zeilen_0, zeilen_1)
        # tmp = '1' if zeile - zeilenzahl < zeilenzahl else '0'
        if zeile - zeilenzahl < zeilenzahl:
            erg += '1'
            inv += '0'
        else:
            erg += '0'
            inv += '1'
        # print(f'Spalte: {spalte + 1}', zeilenzahl, tmp, erg, inv, int('0b' + erg,2), int('0b'+inv,2))
    return int('0b' + erg,2) * int('0b' + inv,2)

def solve2(puzzle):
    spalten = len(puzzle[0])
    erg = ''
    inv = ''
    puzzleorg = puzzle
#    start = 1

    for spalte in range(spalten):
        zeilen = len(puzzle)
        zeilenzahl = 0
        zeilen_0 = []
        zeilen_1 = []
        merke_0 = []

        for zeile in range(zeilen):
            if puzzle[zeile][spalte] == '1':
                zeilenzahl += 1
                zeilen_1.append(puzzle[zeile])
            else:
                zeilen_0.append(puzzle[zeile])
            # print(spalte, zeile, puzzle[zeile], puzzle[zeile][spalte], zeilenzahl)
            print(zeilen_0, zeilen_1)
        if zeile - zeilenzahl < zeilenzahl:
            erg += '1'
            inv += '0'
            puzzle = zeilen_1
        else:
            erg += '0'
            inv += '1'
            puzzle = zeilen_0
        print(f'Spalte: {spalte + 1}', zeilenzahl, erg, inv, int('0b' + erg,2), int('0b'+inv,2))
        # if spalte == 0 and start == 1:
        #     merke_0 = zeilen_0
        #     start = 0
        # print('Merke_0:', merke_0)
        print (int('0b' + erg,2) * int('0b' + inv,2))
        
    return puzzle

puzzle1a = read_puzzle('tag3a.txt')
print(solve2(puzzle1a))