INPUT = 'input'
priorities = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

def priority(lines):
  score = 0   
  for line in lines:
    length = len(line)//2
    first, second = set(line[:length]), set(line[length:])
    letters = first & second
    score += sum([priorities.index(i) for i in letters])
  return score    

def priority2(lines):
  score = 0
  i = 0
  for line in lines:
    if i == 0:
      first = set(line)
    if i == 1:
      second = set(line)
    if i == 2:
      third = set(line)
      letters = first & second & third
      score += sum([priorities.index(i) for i in letters])
      i = 0
      continue
    i += 1
  return score

def main():
  lines = extract_input(INPUT)
  print(priority(lines))
  print(priority2(lines))

if __name__ == '__main__':
  main()
