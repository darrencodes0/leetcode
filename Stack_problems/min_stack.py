class min_stack:

  def __init__(self):
    self.stack = []
    self.min_of_stack = []


  def push(self, x : int):
    self.stack.append(x)

    if not self.min_of_stack:
      self.min_of_stack.append(x)
    else:
      if self.min_of_stack[-1] > x:
        self.min_of_stack.append(x)
  
  def pop(self):
    if not self.isEmpty():
      temp = self.stack[-1]
      del self.stack[-1]
      return temp
    else:
      print("Cannot pop, Stack is empty")

  def isEmpty(self):
    return not self.stack

  def top(self):
    if not self.isEmpty():
      print(self.stack[-1])
    else:
      print("Cannot top, Stack is empty")
    
  def getMin(self):
      print(f"Minimum value: {self.min_of_stack[-1]}")
  
  def print_stack(self):
    print(f"Stack: {self.stack}")
    print(f"Min_Stack: {self.min_of_stack}")
  
if __name__ == '__main__':
  solution = min_stack()
  solution.push(20)
  solution.push(2)
  solution.push(5)
  solution.push(10)
  solution.push(7)
  solution.push(1)
  solution.print_stack()
  solution.top()
  solution.getMin()

"""
REVIEW: 
Using min_stack as it's own stack to track the minimum element in stack, by always appending
the smallest element through comparing it to the number on top of min stack, then
returning it as the smallest number currently in the stack. The regular stack itself has
the regular operations of a typical stack such as pop, push, and top (peek)
"""




    
    













