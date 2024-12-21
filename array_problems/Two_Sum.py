def two_sum(self, target):
    array = [1,3,4,6,7,9,10,2]

    for i in range(len(array)-1):
      for j in range(i+1,len(array)):
        if array[i] + array[j] == target:
          return f"{i}th index: {array[i]}, {j}th index: {array[j]}"

    return "No two sum is possible for target"    