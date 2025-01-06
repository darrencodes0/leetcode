class fizz_buzz:

  def __init__(self):
    self.array = []
 
  def converter(self, n):
    string_list = []

    for number in range(1,n+1,1):
      if number % 5 == 0 and number % 3 == 0:
        string_list.append("FizzBuzz")
      elif number % 5 == 0:
        string_list.append("Buzz")
      elif number % 3 == 0:
        string_list.append("Fizz")
      else:
        string_list.append(str(number))

    return string_list

"""
REVIEW:
Basically using modulus to see if the current number is divisible by 3, 5, or both 3 or 5.
Then print the string that is corresponding with what it's divisible by, if not divisible
by 3 or 5, then just print out the number itself as a string. The list itself can only have
everything as a string or character.
"""








if __name__ == '__main__':
  answer = fizz_buzz()
  print(answer.converter(15))