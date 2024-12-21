import math

def palindrome():
    word = "spekeps"
    l = 0
    h = len(word)-1
    mid = math.floor((l+h)/2)
    counter = h

    for i in range(mid+1):
      if word[counter] == word[i]:
        counter -= 1  
      else:
        return "Word is not a palindrome"
    
    return "Word is a palindrome"

if __name__ == '__main__':
  print(palindrome())