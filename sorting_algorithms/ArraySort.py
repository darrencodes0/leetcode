class ArraySort:
  def __init__(self, array: list):
    if not isinstance(array, list):
      raise TypeError("Suppose to be an array")
    self.array = array
  
  def print_array(self):
    print('[')
    for number in self.array:
      print(f"{number}, ", end=" ")
    print(']')
  
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
      
          
           