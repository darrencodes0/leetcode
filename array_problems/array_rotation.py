def array_rotation(direction : str='right', rotation : int=3):
  array = [1,2,3,4,5,6,7]
  """rotation = rotation % len(array) so if u have 8 rotation and only 7 elements
  in this array, it will only move 1 element from the right. since it went thru a 
  full rotation of 7 already."""
  rotation %= len(array)
  new_list = []

  if direction == 'left':
    new_list = array[rotation:] + array[:rotation]
  elif direction == 'right':
    new_list = array[-rotation:] + array[:-rotation]

  print(new_list)

if __name__ == '__main__':
  print(array_rotation())


    