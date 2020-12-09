import re

def is_valid_password(line):
  line_regex = re.compile(r"(\d+)(-)(\d+)(\s)([a-z])(:)(\s)([a-z]+)")
  mo = re.match(line_regex, line)
  if not mo:
    print(line + ' does not match the regex')
    return False
  ### part 1
  # count_min = int(mo.group(1))
  # count_max = int(mo.group(3))
  # count = mo.group(8).count(mo.group(5))
  # if count_min <= count and count <= count_max:
  #   return True
  # return False

  ### part 2
  idx1 = int(mo.group(1)) - 1
  idx2 = int(mo.group(3)) - 1
  letter = mo.group(5)
  s = mo.group(8)
  if s[idx1] == letter and s[idx2] == letter:
    return False
  elif s[idx1] == letter or s[idx2] == letter:
    return True
  else:
    return False


if __name__ =='__main__':
  ans = 0
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day2/input.txt', 'r') as f:
    for line in f:
      if is_valid_password(line.strip()):
        ans += 1
  print(ans)