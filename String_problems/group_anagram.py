class group_Anagram:

  def _init_(self):
    self.array = []
    
  def sort_anagrams(self, words : list):

    group_anagram = {}

    for word in words:
      sorted_word = tuple(sorted(word))

      if sorted_word not in group_anagram.keys():
        group_anagram[sorted_word] = []
      
      group_anagram[sorted_word].append(word)
    
    return list(group_anagram.values())
  
  '''
    REVIEW:
    Sorts the word then puts into the group_anagram hashmap as its key. for example: cat becomes "act"
    after sorting, and it's put into it as a key. Each other word when sorted becoming "act", will then
    be appended to the list. If the list doesn't exist with that key, add it to the hashmap with that
    sorted word as the key. We convert the sorted_word into a tuple because sorted(word) returns a list
    which is mutable, but a tuple is immutable (can't be changed or modified) so it is allowed as a key
    in the hashmap. Tuple has the same methods as a list.
  '''
  
if __name__ == '__main__':
  solution = group_Anagram()
  print(solution.sort_anagrams(["cat","rat","tac","act","fat","cap"]))

    

  



    




