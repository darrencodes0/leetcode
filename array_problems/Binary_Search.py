import math

class BinarySearch:
  def __init__ (self, array):
    if not isinstance(array, list):
      raise TypeError("Suppose to be an array bro")
    self.array = array

  def binary_search(self, target):
    l = 0
    h = len(self.array) - 1

    while(l <= h):
      mid = math.floor((l+h)/2)

      if self.array[mid] == target:
        return mid
      elif self.array[mid] > target:
        h = mid-1
      else:
        l = mid+1

    return -1
  
  def recursive_binary_search(self, low, high, target):
    if low > high:
      return -1

    mid = math.floor((low+high)/2)

    if self.array[mid] == target:
      return mid
    elif self.array[mid] > target:
      return self.recursive_binary_search(low, mid-1, target)
    else: 
      return self.recursive_binary_search(mid+1, high, target)
    
    """
    REVIEW: 
    recurvisely calls the function and changes low nad high value. Compares
    mid value each time with highs and lows to maintain the bounds of the array effectively
    decreasing the array by half each iteration."""

