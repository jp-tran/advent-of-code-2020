def process_bps(bps):
  ids = []
  for bp in bps:
    if len(bp) == 10:
      ids.append(find_id(bp))
  return ids
  

def find_id(bp):
  return find_row(bp)*8 + find_column(bp)

def find_row(bp):
  ### using binary
  binary = ''
  for char in bp[0:7]:
    if char == 'F':
      binary += '0'
    elif char == 'B':
      binary += '1'
  return int(binary, 2)

  ### using binary search
  # lo = 0
  # hi = 127
  # for char in bp[0:7]:
  #   mid = (hi - lo)//2 + lo
  #   if char == 'F':
  #     hi = mid
  #   elif char == 'B':
  #     lo = mid + 1
  #   else:
  #     print(f'Invalid char: {char}')
  # return lo

def find_column(bp):
  ### convert to binary
  binary = ''
  for char in bp[7:]:
    if char == 'L':
      binary += '0'
    elif char == 'R':
      binary += '1'
  return int(binary, 2)

  ### binary search
  # lo = 0
  # hi = 7
  # for char in bp[7:]:
  #   mid = (hi - lo)//2 + lo
  #   if char == 'L':
  #     hi = mid
  #   elif char == 'R':
  #     lo = mid + 1
  #   else:
  #     print(f'Invalid char: {char}')
  # return lo

def missing_ids(ids):
  ids_set = set(ids)
  missing = []
  for i in range(min(ids), max(ids) + 1, 1):
    if i not in ids_set:
      missing.append(i)
  return missing

if __name__ == "__main__":
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day05/input.txt', 'r') as f:
    bps = [line.strip() for line in f]
    
  ids = process_bps(bps)
  print(missing_ids(ids))