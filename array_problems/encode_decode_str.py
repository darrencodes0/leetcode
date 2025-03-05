array1 = ["##Hello","2darren/","2l5iu"]

def encode(array):
  encoded_word = ""

  for word in array:
    encoded_word += str(len(word)) + "|" + word
  
  return encoded_word

def decode(encoded_word):
  decoded_list = []
  i = 0

  while i < len(encoded_word):
    string = ""
    temp = 0

    if encoded_word[i] == "|":
      length = int(encoded_word[i - 1])
      for j in range(length):
        string += encoded_word[i+1+j]
        temp = j
      decoded_list.append(string)
      i = i + temp

    i += 1

  return decoded_list
  
print(encode(array1))
print(decode(encode(array1)))


"""
Solution:
There can be random words with random cahracters in the list, so putting the a lenght of the string with a # character, and adding it
together into one string, makes it so that you can iterate through that many characters after finding "#" character. 
So even if theres a # after it, it will iterate through it and make it into a string, then append it to the decoded_list. 
It does it until it reaches the end, which it will have added all the words within the one string into the decoded_list.
"""