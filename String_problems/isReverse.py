def reversing_string(self):
    new_word = ""

    for letter in self.reverse[::-1]:
      new_word += letter

    print(new_word)