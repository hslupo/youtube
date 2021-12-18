from time import perf_counter as pfc

def read_puzzle1(file):
  with open(file) as f:
    return list(map(int, f))

def read_puzzle2(file):
  with open(file) as f:
    return [int(x) for x in f]

start = pfc()
puzzle = read_puzzle1('tag1.txt')
mitte = pfc()
puzzle = read_puzzle2('tag1.txt')
ende = pfc()
print(f'Erster Versuch : {(mitte-start) * 1000}')
print(f'Zweiter Versuch: {(ende-mitte) * 1000}')

# Ergebnis uneindeutig
# bei mehrfachen Durchläufen unterschiedliche Zeiten
# und unterschiedliche Sieger

