# main.py

# main.py

# main.py
import random
import time

def checkWin(my_grid):
  returnVal = "|"
  for i in range(3):
    win = False
    for j in range(2):
      if my_grid[i][j] == my_grid[i][j+1] and my_grid[i][j] != " ":
        win = True
      else:
        win = False
        break
    if win:
      returnVal =  my_grid[i][0]
      break
  for j in range(3):
    win = False
    for i in range(2):
      if my_grid[i][j] == my_grid[i+1][j] and my_grid[i][j] != " ":
        win = True
      else:
        win = False
        break
    if win:
      returnVal = my_grid[0][j]
      break
  if my_grid[0][0] == my_grid[1][1] and my_grid[1][1] == my_grid[2][2] and my_grid[0][0] != " ":
    returnVal = my_grid[0][0]
  if my_grid[0][2] == my_grid[1][1] and my_grid[1][1] == my_grid[2][0] and my_grid[0][2] != " ":
    returnVal = my_grid[0][2]
  coveredSquares = 0
  for i in range(0, 3):
    for j in range(0, 3):
      if my_grid[i][j] != " ":
        coveredSquares += 1
        pass
  if coveredSquares == 9:
    return ";"
  return returnVal

def numPossibileWins(possibileWins, my_grid):  
  for i in range(0, 3):
      for j in range(0, 3):
        if my_grid[i][j] != " ":
          continue
        my_grid[i][j] = "O"
        if checkWin(my_grid) == "O":
          possibileWins += 1
          my_grid[i][j] = " "
        else:
          my_grid[i][j] = " "
  return possibileWins
  
def comMoves():
  
  comRow = playerRow - 1
  comColumn = playerColumn - 1
  for i in range(0, 3):
    for j in range(0, 3):
      if my_grid[i][j] != " ":
        continue
      my_grid[i][j] = "O"
      if checkWin(my_grid) == "O":
        print(checkWin(my_grid))
        return
      else:
        my_grid[i][j] = " "

  for i in range(0, 3):
    for j in range(0, 3):
      if my_grid[i][j] != " ":
        continue
      my_grid[i][j] = "X"
      if checkWin(my_grid) == "X":
        my_grid[i][j] = "O"
        return
      else:
        my_grid[i][j] = " "
  for i in range(0, 3):
    for j in range(0, 3):
      if my_grid[i][j] != " ":
        continue
      my_grid[i][j] = "O"
      possibileWins = 0
      possibileWin = numPossibileWins(possibileWins, my_grid)
      if possibileWin == 2:
        print(checkWin(my_grid))
        return
      else:
        my_grid[i][j] = " "
  if my_grid[1][1] == " ":
    my_grid[1][1] = "O"
    return
  for i in range(0, 3, 2):
    for j in range(0, 3, 2):
      if my_grid[i][j] != " ":
        continue
      my_grid[i][j] = "O"
      return
  coveredSquares = 0
  for i in range(0, 3):
    for j in range(0, 3):
      if my_grid[i][j] != " ":
        coveredSquares += 1
        pass
  if coveredSquares == 9:
    return ";"
  while my_grid[comRow][comColumn] != " ":
    print("Hi! Look in the random computer playing algorithim!")
    comRow = random.randint(0, 2)
    comColumn = random.randint(0, 2)
  my_grid[comRow][comColumn] = "O"
  print("Now the computer will play")
  print("Loading...")
  time.sleep(1)
  print("\033c")
  time.sleep(1.5)
  printBoard(my_grid)
      
      

def printBoardPipes(grid, row):
  my_list = []
  for i in range(3):
    my_list.append(" "+grid[row][i]+' ')
    
    my_list.append("|")
  my_list.pop()
  my_string = ''.join(my_list)
  print(my_string)

def printBoardDashes():
  my_list = []
  for i in range(3):
    my_list.append("---")
    
    my_list.append("+")
  my_list.pop()
  my_string = ''.join(my_list)
  print(my_string)
  
def printBoard(grid):
  printBoardPipes(grid, 0)
  printBoardDashes()
  printBoardPipes(grid, 1)
  printBoardDashes()
  printBoardPipes(grid, 2)


my_grid = []


    
def setUpGrid(grid):
  for i in range(3):
    row = []
    for j in range(3):
      row.append(" ")
    grid.append(row)
    
setUpGrid(my_grid)
printBoard(my_grid)

my_grid[1][0] = "O"
my_grid[2][2] = "O"


# Player Moves
while checkWin(my_grid) == "|":
  printBoard(my_grid)
  
  print("Hi! Look in the big while loop at the bottom!")
  playerRow = int(input("Which row would you like to play on:"))
  playerColumn = int(input("Which column would you like to play on:"))
  
  my_grid[playerRow - 1][playerColumn - 1 ] = "X"
  
  printBoard(my_grid)
  
  time.sleep(1)
  # Robot Moves
  comMoves()
  time.sleep(.87)
  print("\033c")
  
  printBoard(my_grid)
  
if checkWin(my_grid) == "X":
  print("Congratulations, I Luigi L. Lemoncello tip my hat before you! YOU WIN!!!!!!!!!")
elif checkWin(my_grid) == "O":
  print("Wompitty, womp womp")
else:
  print("You drawed,  🤨")
