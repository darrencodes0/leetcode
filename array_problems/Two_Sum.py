class two_sum:

  def __init__(self):
    self.array = [3,5,2,1,7,2,9,6,4]

  def two_sum(self, target):
    array = [1,3,4,6,7,9,10,2]

    for i in range(len(array)-1):
      for j in range(i+1,len(array)):
        if array[i] + array[j] == target:
          return f"{i}th index: {array[i]}, {j}th index: {array[j]}"

    return "No two sum is possible for target"    

  def two_sum_hash_map(self, target):
    array = [1,0,4,5,2,3]
    hashmap = {}

    for i in range(len(array)):

      if array[i] in hashmap.keys():
        return [i,hashmap[array[i]]]
      
      hashmap[target-array[i]] = i
      
    """
    REVIEW:
    Adds the complement so if it was 4 in the arra, it would be 2:0. Then when it finds for ex:
    2 in the hashmap, it returns 0 index and element 4 index which would be 2 here.

    This solution would take O(n) because you are looping through the array once
    """

if __name__ == '__main__':
  solution = two_sum()
  print(solution.two_sum_review(6))

"""
Brute force approach:
Two for loops iterate and find when i + j = target
Then return both i index and j index including the values
O(n^2) time complexity
"""