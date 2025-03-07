array1 = [0,3,2,5,4,6,1,1]

no_duplicates = set(array1)

longest_consecutive = 0

for element in no_duplicates:
  temp = 1
  while (element-temp in no_duplicates):
    temp += 1
    longest_consecutive = max(temp, longest_consecutive)

print(longest_consecutive)


"""
Solution:
Put the list of elements into a set to rid of any duplicates to maximize time complexity, then
loop through each element and check how many times you can subtract -1. Each time a element is found
in the no_duplicates set that means there is a consecutive number to it. Then keep matching to see if
the longest_consecutive is > or < temp which tracks the amount of consectuive numbers associated with that value
Get the max out of both, then at the end print out the number for longest_consecutive
"""