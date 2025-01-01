class two_sum:

  def _init_(self):
    self.array = []

  def two_sum(self, target):
    array = [1,3,4,6,7,9,10,2]

    for i in range(len(array)-1):
      for j in range(i+1,len(array)):
        if array[i] + array[j] == target:
          return f"{i}th index: {array[i]}, {j}th index: {array[j]}"

    return "No two sum is possible for target"    

  def two_sum_hash_map(self, target):
    array = [1,3,4,2]
    hashmap = {}

    for i in range(len(array)):

      if target - array[i] in hashmap.keys():
        return [i,hashmap[target - array[i]]]
      
      hashmap[array[i]] = i
    
    """
    REVIEW:
    Adds the element and index into the hashmap, for ex 1:0 and 3:1 from the array.
    It checks to see if the number is in the hashmap, if it is then it returns both
    i current index and the index of the number that was put into the hashmap.
    For ex: 4:2 is placed, then next iteration for 2, if 6-2 = 4 in hashmap.keys()
    which 4 is in the hashmap and has a value of 2. Then index 2 and 3 will be returned
    as the two complements.
    
    This solution would take O(n) because you are looping through the array once
    """


    
    




if __name__ == '__main__':
  solution = two_sum()
  print(solution.two_sum_hash_map(6))

"""
Brute force approach:
Two for loops iterate and find when i + j = target
Then return both i index and j index including the values
O(n^2) time complexity
"""