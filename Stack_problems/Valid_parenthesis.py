class Solution:
  def valid_parenthesis(self):
    word = '({{{{}}}))'
    stack = []

    for bracket in word:
      if stack:
        if stack[-1] == '{' and bracket == '}':
            stack.pop()
        elif stack[-1] == '(' and bracket == ')':
            stack.pop()
        elif stack[-1] == '[' and bracket == ']':
            stack.pop()
        else:
            stack.append(bracket) 
      else:
        stack.append(bracket)

    print(stack)
    
    if stack:
      print("The word is not correct")
    else:
      print("The word is correct")

    """
    Matches each corresponding pairs together, checks top of stack.
    First, if stack is empty it appends the first thing into it.
    if match then pop, if it doesn't match then append to stack with
    symbols like: ), }, ]
    
    At the end after it goes through the entire word:
    If stack is not empty, then return that stack is not correct and
    if empty then it is correct.
    """

if __name__ == '__main__':
   solution = Solution()
   solution.valid_parenthesis()