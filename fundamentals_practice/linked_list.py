class linked_list:
  def __init__(self, data : int, next=None):
    self.data = data
    self.next = next
  
if __name__ == '__main__':
  node1 = linked_list(5)
  node2 = linked_list(6)
  node3 = linked_list(7)

  node1.next = node2
  node2.next = node3

  currentNode = node1

  while True:
    print(currentNode.data, end=" ")
    if currentNode.next is None:
      break
    currentNode = currentNode.next
    print(" -> ", end=" ")

  """
  REVIEW:
  Using while loop with true to create infinite loop, then we check if the currentNode
  node1 has a next, if it doesn't then stop printing and break out of hte loop.
  Then if it does, it sets the currentNode to be the next node, So then node2 will be
  currentNode and it will loop again and print out node2 data now, and repeat.
  """

