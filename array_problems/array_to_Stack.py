def arrayIsStack(self):

    def push(number: int):
      self.stack.append(number)
      print(f'{number} pushed to stack')

    def pop():
      if isEmpty():
        return
      else:
        item_deleted = self.stack[-1]
        del self.stack[-1]
        print(str(item_deleted) + " was popped from the stack")
    
    def isEmpty():
      return len(self.stack) == 0
    
    def peek():
      print(f"Peeking: {self.stack[-1]}")
      self.stack[-1]
    
    def size():
      print(f"Stack size: {str(len(self.stack))}")
    
    push(6)
    push(2)
    push(1)
    push(8)
    push(9)
    push(10)
    pop()
    pop()
    pop()
    peek()
    size()