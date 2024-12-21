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

if __name__ == '__main__':
  solution = isDuplicate()
  print(solution.problem())
