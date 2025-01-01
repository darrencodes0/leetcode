"""
Find Peak Element: Find a peak element in an unsorted array.
Checking both first and last elements as well.
"""

import math

class find_peak:

  def __init__(self):
    self.peak_elements = []
    self.array = [1,3,2,1]

  def find_peak_brute_force(self):
    if self.array[0] > self.array[1]:
      self.peak_elements.append(f"Index: 0, Value: {self.array[0]}")
    if self.array[-1] > self.array[-2]:
      self.peak_elements.append(f"Index: {len(self.array)-1}, Value: {self.array[-1]}")

      
    for i in range(1,len(self.array)-1):
      if self.array[i] > self.array[i+1] and self.array[i] > self.array[i-1]:
        self.peak_elements.append(f"Index: {i}, Value: {self.array[i]}")
  
  def print_peak_elements(self):
    print(self.peak_elements)

  def find_peak_binary_search(self):

    low = 0
    high = len(self.array) - 1
  
    while low < high:
      mid = (low + high) // 2

      if self.array[mid] < self.array[mid+1]:
        low = mid + 1
      else:
        high = mid
      
    return self.array[low]




if __name__ == '__main__':
  solution = find_peak()
  print(solution.find_peak_binary_search())


"""
REVIEW:
Brute Force Approach: Checks both left and right elements and sees if current element
is greater, if it is then append the current element and it's index to the list peak_elements.

UPDATE:
Found O(log n) solution. You could use binary search because it is a sorting algorithm that takes
O(log n) time, but not the typical binary search. My approach: [1,2,3,1]. You get mid = 2 (0 + 3 // 2) here
then check 3, if its greater then low = mid+1. Then mid = 3 (2 + 3 // 2). Then you compare mid = 3 with 
1, it is smaller. That means high = mid. Now low = mid return 3. A way to understand is once mid+1 is greater
than mid, that means the element is definitely on the right side from the original mid. For ex:
[1,2,3,4] vs [1,2,3,1]. 4 is peak of the first array and 3 is peak of the second array, so guaranteed peak is 
on the right. For [1,3,2,1], high becomes 3. Then (0 + 1)/2 = 0. 1 is not greater than 3, so
low = mid + 1. low is now equal to high for index 1. Return 3 which is the peak.
"""