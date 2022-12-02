INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(map(str, file.read().splitlines()))

def get_frequency(strings):
  a = [0]*len(strings[0]) 
  for i in strings:
    for j in range(len(i)):
      a[j] += int(i[j]) 
  a = int(''.join(['1' if i > len(strings)/2 else '0' for i in a]), 2)
  print(bin(a), a)
  return a * (~a & 0b111111111111) 


def main():
  strings = extract_input(INPUT) 
  print(f"The answer to part one is: {get_frequency(strings)}")


if __name__ == '__main__':
  main()
