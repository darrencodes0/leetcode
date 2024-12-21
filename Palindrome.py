def palindrome(self):
    l = 0
    h = len(self.word)-1
    mid = math.floor((l+h)/2)
    counter = h

    for i in range(mid+1):
      if self.word[counter] == self.word[i]:
        counter -= 1  
      else:
        return "Word is not a palindrome"
    
    return "Word is a palindrome"