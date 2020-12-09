from collections import defaultdict

def count_bags(adj):
  def recur(bag, adj, bags):
    if bag not in adj:
      return
    for outer in adj[bag]:
      bags.add(outer)
      recur(outer, adj, bags)
  
  bags = set()  
  recur('shiny gold', adj, bags)
  return len(bags)
  
def count_bags_prt2(adj):
  # dfs returns the number of bags inside bag
  def dfs(bag, adj):
    if bag not in adj:
      return 0
    total = 0
    for inner, count in adj[bag]:
      total += (count + count*dfs(inner, adj))
    return total

  return dfs('shiny gold', adj)

if __name__ == "__main__":
  adj = defaultdict(set)
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day07/input_roman.txt', 'r') as f:
    for line in f:
      words = line.strip().split()
      for i in range(4, len(words), 4):
        adj[words[i+1] + ' ' + words[i+2]].add(words[0] + ' ' + words[1]) # part 1
        # count = 0 if words[i] == 'no' else int(words[i]) # part2
        # adj[words[0] + ' ' + words[1]].add((words[i+1] + ' ' + words[i+2], count)) #part 2
  
  ans = count_bags(adj)
  # ans = count_bags_prt2(adj)
  print(ans)