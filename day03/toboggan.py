def toboggan(hill, right, down):
  num_trees = 0
  i = 0
  for j in range(0, len(hill), down):
    level = hill[j]
    if i >= len(level):
      i = i - len(level)
    if level[i] == '#':
      num_trees += 1
    i += right
  return num_trees


if __name__ =='__main__':
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day3/input.txt', 'r') as f:
    hill = [line.strip() for line in f]
  
  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  trees = []
  for slope in slopes:
    trees.append(toboggan(hill, slope[0], slope[1]))
  
  ans = 1
  for num in trees:
    ans *= num
  
  print(trees)
  print(ans)