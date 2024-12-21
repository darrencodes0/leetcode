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