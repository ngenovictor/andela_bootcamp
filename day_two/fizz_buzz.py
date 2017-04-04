def fizz_buzz(n):
  """A function that returns string "Fizz", 'Buzz', 'FizzBuzz' for 
  numbers that are multiples of 3,5 or both"""
  if n%3==0 and n%5=0:
    return "FizzBuzz"
  elif n%3==0:
    return "Fizz"
  elif n%5==0:
    return "Buzz"
  else:
    return n
