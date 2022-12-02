INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

def most_calories(lines):
  elves = [0]
  curr_sum = 0
  curr_elf = 1
  for i, line in enumerate(lines):
    if line == "":
      elves.append(curr_sum)
      curr_sum = 0
      curr_elf += 1

    else:
      curr_sum += int(line)

  return max(elves)

def top_3_calories(lines):
  elves = [0]
  curr_sum = 0
  curr_elf = 1
  for i, line in enumerate(lines):
    if line == "":
      elves.append(curr_sum)
      curr_sum = 0
      curr_elf += 1

    else:
      curr_sum += int(line)

  print(sorted(elves))

  return sum(sorted(elves)[-3:])


def main():
  lines = extract_input(INPUT)
  print(f"Elf with most calories has: {most_calories(lines)}") 
  print(f"Total of top three elves is: {top_3_calories(lines)}")

if __name__ == '__main__':
  main()
