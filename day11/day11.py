def day11(day, filename):
  with open(f'c:/Users/phuoc/Desktop/coding/advent-of-code/{day}/{filename}', 'r') as f:
    layout = []
    for row in f:
      layout.append([seat for seat in row.strip()])
  
  ans = converge(layout)
  print(ans)
  # print(count_occupied_adj(4, 3, layout))


def first_seat_in_sight(pos, layout, dir):
  i, j = pos
  if i < 0 or i >= len(layout) or j < 0 or j >= len(layout[0]):
    return i, j

  while layout[i][j] == '.':
    if dir == 'topleft':
      i, j = i-1, j-1
    elif dir == 'top':
      i -= 1
    elif dir == 'topright':
      i, j = i-1, j+1
    elif dir == 'left':
      j -= 1
    elif dir == 'right':
      j += 1
    elif dir == 'botleft':
      i, j = i+1, j-1
    elif dir == 'bot':
      i += 1
    elif dir == 'botright':
      i, j = i+1, j+1
    if i < 0 or i >= len(layout) or j < 0 or j >= len(layout[0]):
      return i, j
  return i, j

def count_occupied_adj(i, j, layout): 
  adjacents_start = [(i-1, j-1), (i-1, j), (i-1, j+1), \
        (i, j-1), (i, j+1), \
        (i+1, j-1), (i+1, j), (i+1, j+1)] #for part 1
  positions = ['topleft', 'top', 'topright', 'left', 'right', 'botleft', 'bot', 'botright']
  adjacents = []
  for idx in range(len(positions)):
    r, c = first_seat_in_sight(adjacents_start[idx], layout, positions[idx])
    adjacents.append((r,c))
  
  count = 0
  for row, col in adjacents:
    if 0 <= row < len(layout) and 0 <= col < len(layout[0]):
      if layout[row][col] == '#':
        count += 1
  return count

def advance(layout):
  nxt_state = []
  for i in range(len(layout)):
    row = []
    for j in range(len(layout[0])):
      if layout[i][j] == 'L' and count_occupied_adj(i, j, layout) == 0:
        row.append('#')
      elif layout[i][j] == '#' and count_occupied_adj(i, j, layout) >= 5: #4 for part 1, 5 for part2
        row.append('L')
      else:
        row.append(layout[i][j])
    nxt_state.append(row)
  
  return nxt_state

def count_occuppied(layout):
  count = 0
  for row in layout:
    for seat in row:
      if seat == '#':
        count += 1
  return count

def converge(layout):
  curr = layout
  i = 0
  while True:
    nxt = advance(curr)
    if curr == nxt:
      return count_occuppied(nxt)
    curr = nxt
    # i += 1
    # print(i)


if __name__ == "__main__":
  day11('day11', 'input.txt')
  