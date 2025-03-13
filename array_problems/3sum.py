def three_sum(array: list[int]):
  triplets = []
  sum = 0

  array.sort()

  for i in range(len(array)-1):
    sum = array[i] + array[i+1]
    j = 0

    while j < len(array):
      if j == array[i] or j == array[i+1]:
        pass
      elif sum + array[j] == 0:
        triplets.append([array[i],array[i+1],array[j]])
      j+=1

  """
  look through each pair + 3rd number, and see if its = 0, if it is then append
  to triplets. Keep iterating from i to end of teh array, and j starts at 0
  and always to the end while skipping the two nubmers of i and i+1, since you
  are already adding them."
  """
  sorted_triplets = set()
  for triplet in triplets:
    sorted_triplets.add(tuple(sorted(triplet)))

  sorted_triplets = list(sorted_triplets)

  for i in range(len(sorted_triplets)):
    sorted_triplets[i] = list(sorted_triplets[i])

  """
  Remove dupes and convert it to lists
  """
  
  print(list(sorted_triplets))


three_sum([-1,0,1,2,-1,-4])

"""
My solution: time complexity O(n^2). lOOK AT each pair and add, then third element
we check if adding that = 0, if its does then append to the triplets array. At the
end return it. 

Two-pointers solution:
"""