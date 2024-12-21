def stackToQueue(self):

    def push(number: int):
      self.stack.append(number)
      print(f'{number} pushed to stack')

    def pop():
      if isEmpty():
        return
      else:
        item_deleted = self.stack[-1]
        del self.stack[-1]
        return item_deleted
    
    def isEmpty():
      if self.stack:
        return False
      else:
        return True
    
    def enqueue(number: int):
      push(number)
      self.queue.push(pop())
    
    def dequeue():
      if isEmpty():
        print("Queue is empty")
      else:
        self.queue.pop()