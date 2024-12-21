"""
Find Peak Element: Find a peak element in an unsorted array.
Checking both first and last elements as well.
"""

class find_peak:

  def __init__(self):
    self.peak_elements = []
    self.array = [6,5,1,7,3,2,20,50,2,6,3]
  

  def find_peak(self):
    if self.array[0] > self.array[1]:
      self.peak_elements.append(f"Index: 0, Value: {self.array[0]}")
    if self.array[-1] > self.array[-2]:
      self.peak_elements.append(f"Index: {len(self.array)-1}, Value: {self.array[-1]}")

      
    for i in range(1,len(self.array)-1):
      if self.array[i] > self.array[i+1] and self.array[i] > self.array[i-1]:
        self.peak_elements.append(f"Index: {i}, Value: {self.array[i]}")
  
  def print_peak_elements(self):
    print(self.peak_elements)

if __name__ == '__main__':
  solution = find_peak()
  solution.find_peak()
  solution.print_peak_elements()

"""
REVIEW:
Brute Force Approach: Checks both left and right elements and sees if current element
is greater, if it is then append the current element and it's index to the list peak_elements.

This is brute force approach I created, but there is definitely a way to
optimize it, I will be coming back to this problem later.
"""