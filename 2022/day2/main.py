INPUT = 'input'

key = {
  'AX' : 3+1,
  'BX' : 0+1,
  'CX' : 6+1,
  'AY' : 6+2,
  'BY' : 3+2,
  'CY' : 0+2,
  'AZ' : 0+3,
  'BZ' : 6+3,
  'CZ' : 3+3
}

key2 = {
  'AX' : 0+3,
  'BX' : 0+1,
  'CX' : 0+2,
  'AY' : 3+1,
  'BY' : 3+2,
  'CY' : 3+3,
  'AZ' : 6+2,
  'BZ' : 6+3,
  'CZ' : 6+1
}

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

def rps(lines):
  score = 0
  for line in lines:
    first, second = line.split()
    score += key[f'{first}{second}']
  return score

def wps2(lines):
  score = 0
  for line in lines:
    first, second = line.split()
    score += key2[f'{first}{second}']
  return score

def main():
  lines = extract_input(INPUT)
  print(f"The total score is: {rps(lines)}")
  print(f"The total score for round 2 is {wps2(lines)}")
  

if __name__ == '__main__':
  main()

# very lazy approach

# X - lose
# Y - draw
# Z - win
