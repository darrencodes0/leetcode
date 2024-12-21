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
