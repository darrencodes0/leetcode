class top_k_elements:
  def __init__(self):
    self.array = [4,1,-1,2,-1,2,3]
  

  def top_k_elements_in_list(self, k):
    hashmap = {}
    k_elements = []

    for number in self.array:
      hashmap[number] = hashmap.get(number, 0) + 1

    sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

    for number in sorted_hashmap.keys():
      if k > 0:
        k_elements.append(number)
        k -= 1
    
    
    return k_elements
      


if __name__ == '__main__':
  solution = top_k_elements()
  print(solution.top_k_elements_in_list(2))

  """
  Great explaination using bucket sort:
  https://www.youtube.com/watch?v=YPTqKIgVk-k
  """