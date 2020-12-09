def is_valid_passport(passport):
  # returns true of passport is valid
  curr = set()
  for field in passport:
    curr.add(field[0:3])

  expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  for exp in expected:
    if exp not in curr:
      return False
  return True


if __name__ =='__main__':
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day4/input.txt', 'r') as f:
    passport = []
    count = 0
    iter = 0
    for i, line in enumerate(f):
      if line == '\n':
        if is_valid_passport(passport):
          count += 1
          #debug
          # if 0 < iter < 200: ##
          #   print(passport) ##
        passport = []
        continue
      iter += 1 ##
      passport = passport + line.strip().split(' ')
  
  print(count)