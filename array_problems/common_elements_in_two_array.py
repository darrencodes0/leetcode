"""
Intersection of Two Arrays: Find the common elements in two arrays.
"""
class common_elements:

  def __init__(self, array1: list, array2: list):
    self.array1 = array1
    self.array2 = array2
  
  def intersection(self):
    hashmap = {}
    intersection = set()

    for number in self.array1:
      hashmap[number] = number
    
    for number in self.array2:
      if number in hashmap:
        intersection.add(hashmap[number])
    
    return intersection
    

if __name__ == '__main__':
  solution = common_elements([1,2,2,1],[2,2])
  print(solution.intersection())

  """
  Review:
  Using hash map, I put all the elements from first array into it along with the value
  as it's element so 2:2 or 1:1. Then loop through the 2nd array to check if the number 
  is in the hashmap, if it is append it to the intersection list. We use a set instead
  of a list so we wouldn't get duplicate elements so instead of getting 2 2's, we only
  get a single 2 in the intersection set."""
