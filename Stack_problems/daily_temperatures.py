def daily_temperatures(temperature: list[int]):
  warm_days = []
  for i in range(len(temperature)):
    days = 0
    j = i
    lower_temp_Found = False

    while j < len(temperature):
      if temperature[i] < temperature[j]:
        warm_days.append(days) 
        lower_temp_Found = True
        break
      else:
        j += 1
        days += 1

    if not lower_temp_Found:
        warm_days.append(0)  

  print(warm_days)


    
def daily_temperatures_stack(temperature: list[int]):
  #Make array with 0's with len of temperature array
  warm_days = [0] * len(temperature)
  stack = []

  #enumerate to get the index i, and temp as the element
  for i, temp in enumerate(temperature):
    #only execute when stack has something in it, and the temp in stack is less than temp current
    while stack and stack[-1][0] < temp:
      #gets the value of i which is index
      original_temp = stack[-1][1]
      #subtract current index with original index then append that value to the warm_DAys list
      warm_days[original_temp] = i - original_temp
      #pop it off because we already added it to the warm_days list
      stack.pop()
    
    #append the tuple with temp and i which is index
    stack.append((temp, i))
      
  print(warm_days)


      
      
temperatures = [30,38,30,36,35,40,28]
daily_temperatures(temperatures)
daily_temperatures_stack(temperatures)

"""
My Solution: (brute force)
Each day that passes including on the day, it increments by 1 for each day
checking whether the temperature on teh other days are higher. Once it finds a 
higher, it appends the amount of days it took to find a higher temperature into
a array. If it cannot find any day with higher temperature after it in the list,
it will append 0 so no days is found. I used a boolean value for that.

https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode
Using monotic decreasing order wtih stack
I coded this (daily_temperatures_stack)
"""