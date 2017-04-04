def data_type(n):
  if type(n)==str:
    count = 0
    for t in n:
      count+=1
    return count
  elif not n:
    return "no value"
  elif n == True or n==False:
    return n
  elif type(n)==int:
    if n == 100:
      return "equal to 100"
    elif n > 100:
      return "more than 100"
    else:
      return "less than 100"
  elif type(n)==list:
    if n[2]:
      return n[2]
    else:
      return None