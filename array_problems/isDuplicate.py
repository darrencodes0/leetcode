class isDuplicate:

  def __init__(self):
    self.array = [10,4,2,6,4,1,8,5,9]

  def problem(self):
      hashmap = {}
      duplicatesFound = 0

      for number in self.array:
        hashmap[number] = hashmap.get(number, 0) + 1

      for number, times in hashmap.items():
        if times >= 2:
          duplicatesFound += 1
          return f"There is a duplicate and the number is {number}"
      if duplicatesFound >= 1:
        return "All duplicates found within the array"
      
      return "No duplicates found"
  """
  REVIEW:
  Iterates through entire array and maps the values onto hashmap, the number as the key, followed
  by the value of how many times it appears. I could technically put all of them into a list and
  return all the duplicate numbers, but instead if it detects 2 or more times for the key, then return
  that number as the duplicate. If none are found as having more than 1 occurences, return no duplicates found
  """
  
  def set(self):
    is_there_dupes = set()
    for number in self.array:
      if number in is_there_dupes:
        return f"{number} is a duplicate"
      is_there_dupes.add(number)
    
    return "No duplicates are found"
  
  """
  REVIEW:
  iterate through array and add elements to set, then if a number is detected already in the set. We return
  the number as it is the duplicate. However if we manage to add all the elements into the set, then no duplicates are found
  is returned as the return statement at the end
  """

if __name__ == '__main__':
  solution = isDuplicate()
  print(solution.set())
