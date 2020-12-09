def two_sum(start, end, target, data):
  # returns true if two sum can be found
  seen = set()
  for i in range(start, end + 1):
    diff = target - data[i]
    if diff in seen:
      return True
    seen.add(data[i])
  return False

def part1(data, preamble):
  # returns the first number that doesn't have a two_sum
  for i in range(preamble, len(data)):
    if not two_sum(i - preamble, i - 1, data[i], data):
      return data[i]
  print('All numbers had a two sum')

def part2(data, target):
  for i in range(len(data) - 1):
    for j in range(i+1, len(data)):
      if sum(data[i:j+1]) == target:
        return i, j
  return -1, -1

if __name__ == "__main__":
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day09/input.txt', 'r') as f:
    data = [int(i) for i in f]
  
  # ans1 = part1(data, 25) # part 1
  start, end = part2(data, 393911906) # part 2
  print(min(data[start : end+1]) + max(data[start : end+1]))