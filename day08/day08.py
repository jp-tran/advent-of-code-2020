def get_acc(inst):
  i = 0
  visited = [False for _ in range(len(inst))]
  acc = 0
  while True:
    if i >= len(inst):
      return acc
    visited[i] = True
    if inst[i][:3] == 'nop':
      i += 1
    elif inst[i][:3] == 'acc':
      acc += int(inst[i][4:])
      i += 1
    else:
      i += int(inst[i][4:])
  return acc

def check_program(inst):
  i = 0
  visited = [False for _ in range(len(inst))]
  acc = 0
  while True:
    if i >= len(inst):
      return True
    if visited[i]:
      return False
    visited[i] = True
    if inst[i][:3] == 'nop':
      i += 1
    elif inst[i][:3] == 'acc':
      acc += int(inst[i][4:])
      i += 1
    else:
      i += int(inst[i][4:])
  return True

def brute_force(inst):
  for idx, line in enumerate(inst):
    if line[:3] == 'nop':
      temp = inst[idx]
      inst[idx] = 'jmp ' + line[4:]
      if check_program(inst):
        return inst
      inst[idx] = temp
    elif line[:3] == 'jmp':
      temp = inst[idx]
      inst[idx] = 'nop ' + line[4:]
      if check_program(inst):
        return inst
      inst[idx] = temp

if __name__ == "__main__":
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day08/input.txt', 'r') as f:
    inst = [line.strip() for line in f]

  working_inst = brute_force(inst)
  acc = get_acc(working_inst)
  print(acc)