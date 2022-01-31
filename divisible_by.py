#Check if a number is a divisible by another number

def divisible_by_division(target, divider):
  target, divider = float(target), float(divider)
  is_ended=False
  while not is_ended:
    target = target/divider
    try:
      int(target)
    except:
      is_ended=True
    if target <= 1.0:
      is_ended=True
  if target==1:
    return True
  else:
    return False
  
  
def divisible_by_substraction(target, divider):
  is_ended=False
  while not is_ended:
    target = target-divider
    if target <= 0.0:
      is_ended=True
  if target==0:
    return True
  else:
    return False
  
  
  def divisible_by_ifs(target, divider):
    if divider==2:
      last_digit = int(str(target)[-1])
      if last_digit==0:
        return True
      if last_digit==1:
        return False
      if last_digit==2:
        return True
      if last_digit==3:
        return False
      if last_digit==4:
        return True
      if last_digit==5:
        return False
      if last_digit==6:
        return True
      if last_digit==7:
        return False
      if last_digit==8:
        return True
      if last_digit==9:
        return False
    if divider==3:
      all_digits = [int(one_char) for one_char in str(target)]
      if sum(all_digits) == 0:
        return True
      if sum(all_digits) == 3:
        return True
      if sum(all_digits) > 3:
        all_digits = [int(one_char) for one_char in str(sum(all_digits))]
        if sum(all_digits) == 0:
          return True
        if sum(all_digits) == 3:
          return True
        if sum(all_digits) > 3:
          all_digits = [int(one_char) for one_char in str(sum(all_digits))]
          if sum(all_digits) == 0:
            return True
          if sum(all_digits) == 3:
            return True
      return False
    if divider == 4:
      pass
        
      
