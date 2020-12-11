def find_diffs(arr):
  diff1 = 0
  diff2 = 0
  diff3 = 0
  for i in range(1, len(arr)):
    diff = arr[i] - arr[i-1]
    if diff == 1:
      diff1 += 1
    elif diff == 2:
      diff2 += 1
    elif diff == 3:
      diff3 += 1
  print(diff1, diff3)
  return diff1 * diff3

def arrangements(arr):
  # memo = {arr[-1]: (1, 0)}
  # return dfs(arr, 1, memo)
  ways_to_reach = {i: 0 for i in arr}
  ways_to_reach[0] = 1
  for num in arr:
    for i in range(1, 4):
      if num + i in ways_to_reach:
        ways_to_reach[num+i] += ways_to_reach[num]
  return ways_to_reach[num]

# def can_remove(arr, i):
#   if i == len(arr) - 1:
#     return False
#   if arr[i-1] + 3 >= arr[i+1]:
#     return True
#   return False
 
# def dfs(arr, i, memo):
#   if arr[i] in memo:
#     w = memo[arr[i]][0]
#     wo = 0
#     if can_remove(arr, i):
#       wo = memo[arr[i]][1]
#   else:
#     w = dfs(arr, i+1, memo)
#     wo = 0
#     if can_remove(arr, i):
#       wo = dfs(arr[:i] + arr[i+1:], i, memo)
#     memo[arr[i]] = (w, wo)
#   return w + wo

def day10(day, filename):
  with open(f'c:/Users/phuoc/Desktop/coding/advent-of-code/{day}/{filename}', 'r') as f:
    data = [int(i) for i in f]
  data.append(0)
  data.sort()
  data.append(data[-1] + 3)
  # an1s = find_diffs(data)
  ans2 = arrangements(data)
  print(ans2)

if __name__ == "__main__":
  day10('day10', 'input.txt')
  