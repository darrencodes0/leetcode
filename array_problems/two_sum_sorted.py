
def hashmap_solution(array1: list[int], target: int):
  hashmap = {}

  for i in range(len(array1)):
    complement = target-array1[i]
    hashmap[array1[i]] = complement
    if array1[i] == hashmap.get(target-array1[i]):
      if array1[i] > complement:
        return ([complement, array1[i]])
      else:
        return ([array1[i], complement])

"""
This is the same as two sum, except the array is sorted 
in non-decreasing order (ascending order)
I used hashmap to solve at the top, however you can use two-pointer technique
here.
"""

def two_pointer(array1: list[int], target):
  left = 0
  right = len(array1)-1
  while left < right:
    if array1[left] + array1[right] == target:
      return [array1[left],array1[right]]
    elif array1[left] + array1[right] > target:
      right -= 1
    else:
      left += 1

"""
Two-pointer solution, using left and right indices from index 0 and
the last index. We see if the sum is greater or less than the target.
If the sum is greater, then we need to decrease the right index to go to a 
lower value to add. If the sum is less than target, then we need to increase
left index for a higher value to add. (ONLY WORKS ON SORTED ARRAYS,
meanwhile the hashmap_solution works on both unsorted and sorted arrays.)
"""

#print(hashmap_solution([1,2,3,4], 5))
print(two_pointer([1,2,3,5,7],7))
