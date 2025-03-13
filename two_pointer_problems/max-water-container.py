
array = [1,7,2,5,4,7,3,6]
left = 0
right = len(array) - 1
max_size = 0

while left < right:
  if array[left] > array[right]:
    current_size = (right - left) * array[right]
    max_size = max(current_size,max_size)
    right -= 1
  else:
    current_size = (right - left) * array[left]
    max_size = max(current_size,max_size)
    left += 1
  
print(max_size)

"""
Solution: TO find the water container, it is the minimum value (height) multiplied by the right-left, which
finds the width of the container. You need to find which value of left or right is smaller, then
you can multiply to find the current_size of the container and use max() function with current_size
and any of the previous water containers you found to be the previous max, to see if the current one is
bigger than the previous max. If it is then set that to the max_size water container now.
"""