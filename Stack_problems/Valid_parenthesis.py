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
    Matches each corresponding pairs together, checks top of stack 
    if match then pop, if it doesn't match then append to stack.
    If stack is not empty, then return that stack is not correct and
    if empty then it is correct."""