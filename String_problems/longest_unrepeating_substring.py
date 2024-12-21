"""
  (REVIEW)
  Basically adds each letter to charSet, when it finds s[r] is in the charSet already
  deletes s[l] and keeps incrementing until that character does not match s[r]
  then add s[r] into the charSet. Each time max is also constantly checked to get
  the maximum length of the longest non-repeating sub-string since it can occur
  anytime in-between and at the end. We use a set instead of a list because
  set is O(1) since it uses hash function compared to O(n) when removing an element."""

def longest_substring_ever():
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
  
  return max_substring

if __name__ == '__main__':
  print(longest_substring_ever())