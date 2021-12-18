"""
Das U-Boot scheint bereits einen geplanten Kurs zu haben (Ihre Rätseleingabe).
Sie sollten wahrscheinlich herausfinden, wohin es führt. Beispielsweise:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Ihre horizontale Position und Tiefe beginnen beide bei 0.
Die obigen Schritte würden sie dann wie folgt ändern:

forward 5addiert 5zu Ihrer horizontalen Position insgesamt 5.
down 5trägt 5zu Ihrer Tiefe bei, was zu einem Wert von führt 5.
forward 8addiert 8zu Ihrer horizontalen Position insgesamt 13.
up 3verringert Ihre Tiefe um 3, was zu einem Wert von führt 2.
down 8trägt 8zu Ihrer Tiefe bei, was zu einem Wert von führt 10.
forward 2addiert 2zu Ihrer horizontalen Position insgesamt 15.

Nachdem Sie diese Anweisungen befolgt haben, haben Sie eine horizontale Position von 15und eine Tiefe von 10.
(Wenn man diese miteinander multipliziert, erhält man 150.)

****************************************************************************
Puzzle 2
Zusätzusätzlich zur horizontalen Position und Tiefe müssen Sie noch einen dritten Wert verfolgen,
den Zielpunkt, der ebenfalls bei 0 beginnt. Die Befehle bedeuten auch etwas ganz anderes, als Sie zunächst dachten:

down X - erhöht dein Ziel um X Einheiten.
up X - verringert dein Ziel um X Einheiten.
forward X macht zwei Dinge:
    Es erhöht Ihre horizontale Position um X Einheiten.
    Es erhöht Ihre Tiefe um Ihr Ziel multipliziert mit X .
Beachten Sie wieder, dass, da Sie auf einem U - Boot sind, down und up tut das Gegenteil von dem,
was man erwarten könnte: „down“ Mittel in der positiven Richtung zielen.

Das obige Beispiel macht jetzt etwas anderes:

forward 5 - addiert 5 zu Ihrer horizontalen Position insgesamt 5.
            Da Ihr Ziel ist 0, ändert sich Ihre Tiefe nicht.
down 5 -    trägt 5 zu Ihrem Ziel bei, was zu einem Wert von 5.
forward 8   addiert 8 zu Ihrer horizontalen Position insgesamt 13.
            Weil Ihr Ziel ist 5, erhöht sich Ihre Tiefe um 8*5=40.
up 3        verringert Ihr Ziel um 3, was zu einem Wert von führt 2.
down 8      trägt 8 zu Ihrem Ziel bei, was zu einem Wert von 10.
forward 2   addiert 2 zu Ihrer horizontalen Position insgesamt 15.
            Da Ihr Ziel ist 10, erhöht sich Ihre Tiefe um 2*10=20insgesamt 60.

Nachdem Sie diese neuen Anweisungen befolgt haben, haben Sie eine horizontale Position von 15 und eine Tiefe von 60.
(Wenn man diese multipliziert, erhält man 900.)

"""

def read_puzzle(file):
  with open(file) as f:
    return f.read().split("\n")

def solve_puzzle2(puzzle):   # eigener versuch
  # liste of int
  position = tiefe = ziel = 0
  for nr in puzzle:
    # print(puzzle[nr], anzahl)
    richtung, za = nr.split()
    zahl = int(za)
    if richtung == "forward":
      position += zahl
      tiefe += ziel * zahl
    elif richtung == "down":
      ziel += zahl
      # tiefe += zahl
    elif richtung == "up":
      ziel -= zahl
      # tiefe -= zahl
    print(richtung, zahl, position,tiefe,ziel)
  return position * tiefe


def solve_puzzle1(puzzle):   # eigener versuch
  # liste of int
  position = tiefe = 0
  for nr in puzzle:
    # print(puzzle[nr], anzahl)
    richtung, za = nr.split()
    zahl = int(za)
    if richtung == "forward":
      position += zahl
    elif richtung == "down":
      tiefe += zahl
    elif richtung == "up":
      tiefe -= zahl
  return position * tiefe

puzzle = read_puzzle('tag2.txt')
print(solve_puzzle2(puzzle))




