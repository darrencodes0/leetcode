class Stack:

  def __init__(self, notation_list: str):
    self.stack = []
    self.notation_list = notation_list

  def push(self, item: str):
    self.stack.append(item)

  def pop(self):
    if self.stack:
      temp = self.stack[-1]
      del self.stack[-1]
      return temp

  def seeAll(self):
    print(self.stack)

  def polish_notation(self):

    for element in self.notation_list:
      if element == '*':
        self.push(self.pop() * self.pop())
      elif element == '/':
        first = self.pop()
        second = self.pop()
        self.push(second / first)
      elif element == '+':
        self.push(self.pop() + self.pop())
      elif element == '-':
        first = self.pop()
        second = self.pop()
        self.push(second - first)
      else:
        self.push(int(element))
      
    return self.pop()



if __name__ == '__main__':
  stack = Stack(["4","13","5","/","+"])
  print(stack.polish_notation())


"""
The leetcode problem:
https://neetcode.io/problems/evaluate-reverse-polish-notation

Solution: Iterate through the notation_list and keep pushing the numbers into stack
until you find any of the operators, then you pop off the two numbers and execute
the operation on them. Push the result back onto the stack. You want to keep
two numbers on the stack at all times so the next operator can perform operations
on it with the other number. Also the number you push back onto the stack is the
sum, that you will eventually return at the end of the stack. O(n) time complexity. 
"""