import numpy as np

def day12(day, filename):
  with open(f'c:/Users/phuoc/Desktop/coding/advent-of-code/{day}/{filename}', 'r') as f:
    directions = []
    for line in f:
      dir = line.strip()
      directions.append((dir[0], float(dir[1:])))

  print(move2(directions))

### part 1
def commands():
  return {
    'N': lambda x, y, dist: (x, y + dist),
    'S': lambda x, y, dist: (x, y - dist),
    'E': lambda x, y, dist: (x + dist, y),
    'W': lambda x, y, dist: (x - dist, y),
    'L': lambda curr_ori, d_ori: (curr_ori + d_ori)%360,
    'R': lambda curr_ori, d_ori: (curr_ori - d_ori)%360,
    'F': lambda x, y, dist, ori: (x + dist*np.cos(np.deg2rad(ori)), y + dist*np.sin(np.deg2rad(ori)))
  }

def move(directions):
  ori = 0 # initial orientation
  process = commands()
  x = y = 0
  for command, val in directions:
    function = process[command]
    if command == 'L' or command == 'R':
      ori = function(ori, val)
    elif command in set(['N', 'S', 'E', 'W']):
      (x, y) = function(x, y, val)
    elif command == 'F':
      (x, y) = function(x, y, val, ori)
    # print(x, y)
  
  return abs(x) + abs(y)

### part 2
def commands2():
  return {
    'N': lambda wx, wy, dist: (wx, wy + dist),
    'S': lambda wx, wy, dist: (wx, wy - dist),
    'E': lambda wx, wy, dist: (wx + dist, wy),
    'W': lambda wx, wy, dist: (wx - dist, wy),
  }

def rotate_wp(wx, wy, val, dir):
  d = np.sqrt(wx**2 + wy**2)
  sign = 1 if dir == 'L' else -1
  phi = np.arctan2(wy, wx) #in radians, in the range [-pi, pi]
  if phi < 0:
    phi = 2*np.pi + phi #convert to range [0, 2*pi]
  x = d*np.cos(np.deg2rad(val)*sign + phi)
  y = d*np.sin(np.deg2rad(val)*sign + phi)
  return (x, y)

def move_forward(x, y, wx, wy, val):
  x = x + wx*val
  y = y + wy*val
  return (x, y)
  
def move2(directions):
  process = commands2()
  x = y = 0
  wx = 10.0
  wy = 1.0
  for command, val in directions:
    if command == 'L' or command == 'R':
      (wx, wy) = rotate_wp(wx, wy, val, command)
    elif command in set(['N', 'S', 'E', 'W']):
      function = process[command]
      (wx, wy) = function(wx, wy, val)
    elif command == 'F':
      (x, y) = move_forward(x, y, wx, wy, val)
    # print(command, val, round(x), round(y), round(wx), round(wy))
  
  return round(abs(x)) + round(abs(y))

if __name__ == "__main__":
  day12('day12', 'input.txt')
  