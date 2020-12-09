def two_sum(nums, total):
  num_set = set()
  for num in nums:
    diff = total - num
    if diff in num_set:
      return diff, num
    num_set.add(num)

if __name__ == '__main__':
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day1/input.txt', 'r') as f:
    nums = [int(num.strip()) for num in f]
  n1, n2 = two_sum(nums, 2020)
  print(n1*n2)