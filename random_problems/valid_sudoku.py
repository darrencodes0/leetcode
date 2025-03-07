import random

class Solution:
  def valid_sudoku(self,char):

    for i in range(9):
      # row and column sets for each individual column/row to check for dupes
      row = set()
      column = set()

      for j in range(9):
        #checks if dupes exist in each row
        if char[i][j] != "." and char[i][j] in row:
          return False
        row.add(char[i][j])
        #checks if dupes exist in each column
        if char[j][i] != "." and char[j][i] in column:
          return False
        column.add(char[j][i])
    
    #to check each 3x3 grids inside the sudoku board, since theres 9 of em
    for i in range(0, 9, 3):
      for j in range(0, 9, 3):
        subgrid = set()

        for n in range(i,i+3):
          for m in range(j,j+3):
            if char[n][m] != "." and char[n][m] in subgrid:
              return False
            subgrid.add(char[n][m])

    return True
        





if __name__ == '__main__':
  solution = Solution()

  char = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
  ]
  
  print(solution.valid_sudoku(char))

  """
  Solution:
  Iterating through both columns and rows using a set for both , and checking
  to see if theres dupes since in sudoku u can only have 1 number of each from
  1-9. Then getting the subgrids 3x3 of the sudoku board. Finding 3x3 and then iterating
  through each grid with one set and checking if all the numbers in the 3x3 can
  only have 1 1-9 number. Then return true if sudoku board is valid and false if there is any
  dupe in rows/columns or dupes in 3x3 grids.
  """