import math

class LeetCode:
  
  def __init__(self):
    self.word = "abba"
    self.reverse = "hello"
    self.array = [1,5,2,3,6,5,8,6,4]
    self.stack = []
    self.queue = []

  def palindrome(self):
    l = 0
    h = len(self.word)-1
    mid = math.floor((l+h)/2)
    counter = h

    for i in range(mid+1):
      if self.word[counter] == self.word[i]:
        counter -= 1  
      else:
        return "Word is not a palindrome"
    
    return "Word is a palindrome"
    
  def arrayIsStack(self):

    def push(number: int):
      self.stack.append(number)
      print(f'{number} pushed to stack')

    def pop():
      if isEmpty():
        return
      else:
        item_deleted = self.stack[-1]
        del self.stack[-1]
        print(str(item_deleted) + " was popped from the stack")
    
    def isEmpty():
      return len(self.stack) == 0
    
    def peek():
      print(f"Peeking: {self.stack[-1]}")
      self.stack[-1]
    
    def size():
      print(f"Stack size: {str(len(self.stack))}")
    
    push(6)
    push(2)
    push(1)
    push(8)
    push(9)
    push(10)
    pop()
    pop()
    pop()
    peek()
    size()
    
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

  def reversing_string(self):
    new_word = ""

    for letter in self.reverse[::-1]:
      new_word += letter

    print(new_word)

  def isAnagram(self):
    first_word = "sjokera"
    second_word = "kojreas"

    first_word_map = {}
    second_word_map = {}

    """
    Puts in the letter into the hashmaps, if it doesn't exist start from 0, if it does add 1
    """
    for letter in first_word:
      first_word_map[letter] = first_word_map.get(letter, 0) + 1

    for letter in second_word:
      second_word_map[letter] = second_word_map.get(letter, 0) + 1

    """
    Checks if the two hashmaps have the same keys, and same values for each key
    """
    if first_word_map == second_word_map:
      return "Both words are anagrams"
    else:
      return "Both words are not anagrams"
  
  def two_sum(self, target):
    array = [1,3,4,6,7,9,10,2]

    for i in range(len(array)-1):
      for j in range(i+1,len(array)):
        if array[i] + array[j] == target:
          return f"{i}th index: {array[i]}, {j}th index: {array[j]}"

    return "No two sum is possible for target"    
  
  def time_to_buy_stocks(self):
    min_price = float('inf')
    max_profit = 0
    days = [7,5,3,6,2,10,8]

    for price in days:
      if price < min_price:
        min_price = price
      
      if max_profit < price - min_price:
        max_profit = price - min_price
      
    return f"Maximum profit: {max_profit}"
  
  """ 
  (REVIEW)
  Basically find the minimum price on a buy day, then see if the next days have 
  a lower price to find a new buy day, then find the profit margin. If profit
  margin is greater than before, it is the new maximum profit.
  At the end it will find the max profit and return it
  """

  def array_rotation(self, direction='right', rotation=3):
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
    
  """
  (REVIEW)
  Basically adds each letter to charSet, when it finds s[r] is in the charSet already
  deletes s[l] and keeps incrementing until that character does not match s[r]
  then add s[r] into the charSet. Each time max is also constantly checked to get
  the maximum length of the longest non-repeating sub-string since it can occur
  anytime in-between and at the end. We use a set instead of a list because
  set is O(1) since it uses hash function compared to O(n) when removing an element."""

  def longest_substring_ever(self):
    word = "pwwkew"
    character_set = set()
    l = 0
    max_substring = 0
    
    for i in range(len(word)):
      while word[i] in character_set:
        character_set.remove(word[l])
        l += 1
      character_set.add(word[i])
      max_substring = max(max_substring, i - l + 1)
    
    print(max_substring)

  def valid_parenthesis(self):
    word = '({{{{}}}))'
    stack = []
  
    for bracket in word:
      if stack:
        if stack[-1] == '{' and bracket == '}':
            stack.pop()
        elif stack[-1] == '(' and bracket == ')':
            stack.pop()
        elif stack[-1] == '[' and bracket == ']':
            stack.pop()
        else:
            stack.append(bracket) 
      else:
        stack.append(bracket)

    print(stack)
    
    if stack:
      print("The word is not correct")
    else:
      print("The word is correct")

    """
    Matches each corresponding pairs together, checks top of stack 
    if match then pop, if it doesn't match then append to stack.
    If stack is not empty, then return that stack is not correct and
    if empty then it is correct."""

  def stackToQueue(self):

    def push(number: int):
      self.stack.append(number)
      print(f'{number} pushed to stack')

    def pop():
      if isEmpty():
        return
      else:
        item_deleted = self.stack[-1]
        del self.stack[-1]
        return item_deleted
    
    def isEmpty():
      if self.stack:
        return False
      else:
        return True
    
    def enqueue(number: int):
      push(number)
      self.queue.push(pop())
    
    def dequeue():
      if isEmpty():
        print("Queue is empty")
      else:
        self.queue.pop()


if __name__ == '__main__':
  solution = LeetCode()
  solution.stackToQueue



'''
1. Arrays and Strings
Two Sum: Find two numbers in an array that add up to a target.
Best Time to Buy and Sell Stock: Maximize profit by buying and selling stocks.
Rotate Array: Rotate an array by k steps.
Valid Anagram: Check if two strings are anagrams.
Longest Substring Without Repeating Characters: Find the longest substring with unique characters.
2. Linked Lists
Reverse Linked List: Reverse a singly linked list.
Detect Cycle in Linked List: Check if a linked list has a cycle.
Merge Two Sorted Lists: Merge two sorted linked lists into one.
Palindrome Linked List: Check if a linked list is a palindrome.
3. Stacks and Queues
Valid Parentheses: Check if parentheses in a string are balanced.
Min Stack: Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement Queue Using Stacks: Implement a queue using two stacks.
4. Hash Tables
Two Sum (HashMap): Same as in arrays but using a hashmap for faster lookups.
Group Anagrams: Group a list of strings into anagram groups.
Intersection of Two Arrays: Find the common elements in two arrays.
Count Distinct Substrings: Count the number of distinct substrings in a string.
5. Sorting and Searching
Binary Search: Search for a value in a sorted array.
Merge Intervals: Merge overlapping intervals in an array.
Find Peak Element: Find a peak element in an unsorted array.
Quick Sort/Merge Sort: Implement these sorting algorithms.
6. Dynamic Programming
Climbing Stairs: Count the number of ways to reach the top of a staircase.
House Robber: Maximize the amount of money you can rob from houses without robbing two adjacent houses.
Longest Common Subsequence: Find the longest subsequence common to two strings.
Knapsack Problem: Solve the 0/1 knapsack problem.
7. Trees and Graphs
Binary Tree Inorder Traversal: Traverse a binary tree in inorder.
Level Order Traversal: Perform a level-order traversal (breadth-first search) of a binary tree.
Lowest Common Ancestor of a Binary Search Tree: Find the lowest common ancestor of two nodes in a BST.
Graph Traversals: BFS (breadth-first search) and DFS (depth-first search) on graphs.
Number of Islands: Count the number of connected components (islands) in a 2D grid.
8. Backtracking
Permutations: Generate all permutations of a list of numbers or characters.
Subsets: Generate all subsets of a set (including the empty set).
N-Queens: Solve the N-Queens problem using backtracking.
Combination Sum: Find all combinations of numbers that add up to a target.
9. Mathematical Problems
Reverse Integer: Reverse the digits of an integer.
Palindrome Number: Check if a number is a palindrome.
Sqrt(x): Compute the square root of a number without using built-in functions.
Count Primes: Count the number of prime numbers less than a given number.
10. Bit Manipulation
Single Number: Find the element that appears only once in an array where every other element appears twice.
Hamming Distance: Calculate the Hamming distance between two integers.
Power of Two: Check if a number is a power of two.
11. Sliding Window
Maximum Subarray: Find the contiguous subarray with the largest sum.
Longest Substring with K Distinct Characters: Find the longest substring with at most K distinct characters.
Minimum Size Subarray Sum: Find the minimal length of a contiguous subarray whose sum is at least a given value.
Tips for Preparation:
Practice with Constraints: Be mindful of time and space complexity. Often, you'll need to optimize brute-force solutions.
Understand the Algorithm: Don’t just memorize solutions. Understand the underlying algorithms, as interviewers may ask you to explain or modify them.
Edge Cases: Always think about edge cases, like empty arrays, strings, or null values, and handle them in your solutions.
Focusing on these key topics will give you a solid foundation for your first CS internship interview. Good luck with your preparation! Let me know if you'd like detailed explanations or examples of any specific question.
'''