def arrayToQueue(self):

    def enqueue(number):
      self.queue.append(number)

    def dequeue():
      del self.queue[0]
    
    def peek():
      print(str(self.queue[0]))
    
    def isEmpty():
      if len(self.queue):
        print("False")
      else:
        print("True")
    
    def size():
      print(len(self.queue))
    
    def clear():
      self.queue.clear()

    enqueue(5)
    enqueue(10)
    enqueue(2)
    dequeue()
    isEmpty()
    print(self.queue)
    size()