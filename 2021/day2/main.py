INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(map(str, file.read().splitlines()))

class submarine:

  def __init__(self):
    self.x, self.y = 0, 0
    self.aim = 0

  def move(self, command):
    op, num = command.split(' ')
    num = int(num)
    if op == 'up':
      self.y -= num
    elif op == 'down':
      self.y += num
    elif op == 'forward':
      self.x += num

  def correct_move(self, command):
    op, num = command.split(' ')
    num = int(num)
    
    if op == 'down':
      self.aim += num
    elif op == 'up':
      self.aim -= num
    elif op == 'forward':
      self.x += num
      self.y += self.aim * num


def main():

  commands = extract_input(INPUT)

  sub  = submarine()
  sub2 = submarine()

  for i in commands:
    sub.move(i)
    sub2.correct_move(i)

  print(f"Final position of sub is ({sub.x}, {sub.y})")
  print(f"First answer is {sub.x * sub.y}")
  
  print(f"Final position of sub2 is ({sub2.x}, {sub2.y})")
  print(f"First answer is {sub2.x * sub2.y}")

if __name__ == '__main__':
  main()
