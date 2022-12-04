INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())


def main():
  lines = extract_input(INPUT)

if __name__ == '__main__':
  main()
