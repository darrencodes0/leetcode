class queue:

  def __init__(self):
    self.stack = []
    self.queue = []

  def push(self, number: int):
    self.stack.append(number)

  def pop(self):
    if self.stack:
      item_deleted = self.stack[-1]
      del self.stack[-1]
      return item_deleted
    else:
      print("Cannot pop off stack, it is empty")

  def isEmpty(self):
    return not self.stack and not self.queue
  
  def enqueue(self, number: int):
    self.push(number)
       
  
  def dequeue(self):
    if not self.queue:
      while self.stack:
        self.queue.append(self.pop())
    
    if self.queue:
      del self.queue[-1]
  
  def printStack_Queue(self):
    print(f"Stack: {self.stack}")
    print(f"Queue: {self.queue}")
      

if __name__ == '__main__':
  solution = queue()
  solution.enqueue(10)
  solution.enqueue(20)
  solution.enqueue(30)
  solution.dequeue()
  solution.enqueue(50)
  solution.dequeue()
  solution.dequeue()
  solution.enqueue(100)
  solution.dequeue()
  solution.dequeue()

  print(solution.printStack_Queue())

  '''
  REVIEW: Using two stacks to create a queue. Enqueue pushes numbers into
  first stack. Then dequeue checks if queue is empty before appending all
  numbers into the queue from first stack till its empty. It reverses the order
  10-15-20 to 20-15-10 so 10 is the first element to get popped off. Then it pops
  off every time until its empty, then if theres anything on the stack again
  from enqueuing it will append them to the queue again and prepare for dequeuing.'''
  