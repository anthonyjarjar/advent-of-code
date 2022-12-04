INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

def contained_range(lines):
  result = 0
  for line in lines:
    elves = line.split(',')
    for i in range(2):
      elves[i] = list(map(int, elves[i].split('-')))
    
    if ((elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][1]) or 
       (elves[1][0] <= elves[0][0] and elves[1][1] >= elves[0][1])):
      result += 1
  return result

def overlapping_range(lines):
  result = 0
  for line in lines:
    elves = line.split(',')
    for i in range(2):
      elves[i] = list(map(int, elves[i].split('-')))

    if ((elves[1][0] in range(elves[0][0], elves[0][1]+1)) or
        (elves[0][0] in range(elves[1][0], elves[1][1]+1))):
        result += 1
  return result 

def main():
  lines = extract_input(INPUT)
  print(f"Question 1: {contained_range(lines)}")   
  print(f"Question 2: {overlapping_range(lines)}")

if __name__ == '__main__':
  main()
