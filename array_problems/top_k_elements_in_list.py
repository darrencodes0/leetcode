class top_k_elements:
  def __init__(self):
    self.array = [1,2,2,3,3,3,4,4,4]
  

  def top_k_elements_in_list(self, k):
    hashmap = {}
    bucket = [[] for number in range(len(self.array)+1)]
    return_list = []

    for number in self.array:
      hashmap[number] = hashmap.get(number, 0) + 1

    for key, value in hashmap.items():
      bucket[value].append(key)
    
    for i in range(len(bucket)-1,0,-1):
      for number in bucket[i]:
        if k > 0:
          return_list.append(number)
          k -= 1
        else:
          return return_list
    
    return return_list



  
    



      


if __name__ == '__main__':
  solution = top_k_elements()
  print(solution.top_k_elements_in_list(3))

  """
  Great explaination using bucket sort:
  https://www.youtube.com/watch?v=YPTqKIgVk-k
  """