def day4(text):
  reqd = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
  passports = text.split('\n\n')
  has_reqd_keys = 0
  has_valid_data = 0
  for passport in passports:
        field_keys = {field.split(":")[0] for field in passport.split()} 
        # print(field_keys)
        if field_keys & reqd == reqd:
            has_reqd_keys += 1
            has_valid_data += validated_data(passport)

  print(f"Pt1: {has_reqd_keys} all req'd fields")
  print(f"Pt2: {has_valid_data} req'd fields, valid data")

def validated_data(passport):
  valid = 1
  for field in passport.split():
    key = field[:3]
    data = field[4:]

    if key == 'byr':
      valid = len(data) == 4 and "1920" <= data <= "2002"
    elif key == 'iyr':
      valid = len(data) == 4 and "2010" <= data <= "2020"
    elif key == 'eyr':
      valid = len(data) == 4 and "2020" <= data <= "2030"
    elif key == 'hgt':
      if "cm" in data:
        valid = "150" <= data[:-2] <= "193"
      elif "in" in data:
        valid = "59" <= data[:-2] <= "76"
      else:
        valid = 0
    elif key == 'hcl':
      try:
        int(data[1:], 16)
        valid = data[0] == "#"
      except ValueError:
          valid = 0
    elif key == 'ecl':
      valid_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
      valid = data in valid_colors
    elif key == 'pid':
      valid = len(data) == 9 and data.isdigit()

    if not valid:
      return valid

  return valid

if __name__ == "__main__":
  with open('c:/Users/phuoc/Desktop/coding/advent-of-code/day04/input.txt', 'r') as f:
    text = [line for line in f]
    text = "".join(text)
  day4(text)