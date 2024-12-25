import math

class ArraySort:
  def __init__(self, array: list=None):
    if array is None:
      self.array = []
    elif not isinstance(array, list):
      raise TypeError("Suppose to be an array")
    else:
      self.array = array
  
  def print_array(self, array):
     print(array)
  
  def bubble_sort(self):
    for i in range(len(self.array)-1):
        for j in range(len(self.array) - i - 1):
            if self.array[j] > self.array[j + 1]:
                temp = self.array[j]
                self.array[j] = self.array[j + 1]
                self.array[j + 1] = temp
    return self.array

  def selection_sort(self):
    for i in range(len(self.array)):
      minIndex = i
      for j in range(i+1,len(self.array)):
        if self.array[minIndex] > self.array[j]:
          minIndex = j

      if minIndex != i:
        temp = self.array[i]
        self.array[i] = self.array[minIndex]
        self.array[minIndex] = temp
  
  def merge_sort(self, array):
        if len(array) <= 1:
            return array

        mid = math.floor(len(array) / 2)
        arrayA = self.merge_sort(array[:mid])
        arrayB = self.merge_sort(array[mid:])
        return self.merge(arrayA, arrayB, array)

  def merge(self, arrayA, arrayB, array):
      i = j = k = 0

      while j < len(arrayA) and k < len(arrayB):
          if arrayA[j] < arrayB[k]:
              array[i] = arrayA[j]
              j += 1
          else:
              array[i] = arrayB[k]
              k += 1
          i += 1

      while j < len(arrayA): 
          array[i] = arrayA[j]
          j += 1
          i += 1

      while k < len(arrayB):
          array[i] = arrayB[k]
          k += 1
          i += 1

      return array

  def quick_sort(self, low, high, array):
     
    if low < high:
      partition_value = self.partition(low, high, array)
      self.quick_sort(low, partition_value-1, array)
      self.quick_sort(partition_value+1, high, array)
    
    return array

  """
    REVIEW for Quick Sort:
    Set low = 0, high = len(array) - 1 and input array. It recursively finds the pivot through
    partition. Then using the partition value it recursively calls quick sort so it can continue to find
    pivots. The partition also somewhat sorts the array in that elements on left side of pivot is 
    smaller and elements on the right side of pivot is greater.
    """

  def partition(self, low, high, array):
    i = low - 1
    j = low
    pivotIndex = high

    while j < pivotIndex:
      if array[j] < array[pivotIndex]:
         i += 1
         temp = array[i]
         array[i] = array[j]
         array[j] = temp
      j += 1
      """Move to next j value so the while loop can check it in next iteration"""
    
    i += 1
    temp = array[pivotIndex]
    array[pivotIndex] = array[i]
    array[i] = temp

    return i
  
    """
    REVIEW for Partition:
    No need to check the last element which is THE pivot position (j < pivotIndex). When j value
    is less than pivotIndex, increment i then swap i value with j value. Then increment j 
    and do the same step, until j reaches the pivot.

    When j reaches pivot index it ends the loop. At the end, we increment i value by 1 
    then swap it with the pivot (partition). Return the partition value.
    """
    
    
      
     


if __name__ == '__main__':
    array = [5, 1, 2, 3, 5, 1, 10, 52, 43]
    solution = ArraySort()
    solution.print_array(solution.quick_sort(0, len(array) - 1, array))
