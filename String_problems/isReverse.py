def reversing_string():
    word = "hello"
    new_word = ""

    for letter in word[::-1]:
      new_word += letter

    return new_word

if __name__ == '__main__':
   print(reversing_string())