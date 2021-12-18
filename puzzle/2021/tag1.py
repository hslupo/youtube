

def read_puzzle(file):
  with open(file) as f:
    return list(map(int, f))

def solve_puzzle(puzzle):   # eigener versuch
  # liste of int
  anzahl = 0
  for nr in range(1,len(puzzle)):
    if puzzle[nr] > puzzle[nr-1]:
      anzahl += 1
    # print(puzzle[nr], anzahl)
  return anzahl

def solve_puzzle2(puzzle):   # eigener versuch
  # liste of int
  anzahl = 0
  for nr in range(0,len(puzzle)-3):
    a = puzzle[nr] + puzzle[nr+1] + puzzle[nr+2]
    b = puzzle[nr+1] + puzzle[nr+2] + puzzle[nr+3]
    if b > a:
      anzahl += 1
    # print(puzzle[nr], anzahl)
    print(b, a)
  return anzahl

puzzle = read_puzzle('puzzle_tag1.txt')
lb = [199,200,208,210,200,207,240,269,260,263]
# print(f'Ergebnis: {solve_puzzle(lb)}' )
# print(f'Ergebnis: {solve_puzzle(puzzle)}' )

print(f'Ergebnis: {solve_puzzle2(lb)}' )
print(f'Ergebnis: {solve_puzzle2(puzzle)}' )