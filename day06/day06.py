def customs(groups):
  count = 0
  for group in groups:
    ### part 1
    # questions = set()
    # for person in group.split():
    #   for char in person:
    #     questions.add(char)

    ### part 2
    sets_list = []
    for person in group.split():
      sets_list.append(set(person))
    
    count += len(set.intersection(*sets_list))
  return count

if __name__ == "__main__":
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day06/input.txt', 'r') as f:
    text = [line for line in f]
    text = "".join(text)
    
  groups = text.split('\n\n')
  ans = customs(groups)
  print(ans)