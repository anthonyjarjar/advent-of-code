INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(map(int, file.read().splitlines()))

def num_increasing_values(sweeps):
  increase = 0 
  for i in range(1, len(sweeps)):
    if sweeps[i-1] < sweeps[i]:
      increase += 1
  return increase

def larger_sums(depths):
  increase = 0
  curr, prev = 999999, 0
  for i in range(len(depths) - 2):
    prev = curr
    curr = depths[i] + depths[i+1] + depths[i+2]
    if prev < curr:
      increase += 1
  return increase

def main():
  depths = extract_input(INPUT)
  print(f"There are {num_increasing_values(depths)} measurements larger than the previous measurement.")
  print(f"Increasing sums: {larger_sums(depths)}") 

if __name__ == '__main__':
  main()
