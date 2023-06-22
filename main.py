_author_ = "LuckyPlayzYT"
_date_ = "Tuesday, June 20th, 2023"
_version_ = "1.0"
_filename_ = "Checkers.py"
_description_ = "A Terminal Checkers game in Python"

# Module Imports
from replit import clear
from colorama import Fore
from copy import deepcopy

# CONSTANTS
INTRO = """This is a two-player version of Checkers / Draughts.
Player 1's pieces are marked with an 'x' or an 'X'.
Player 2's pieces are marked with an 'o' or an 'O'.
Empty Spaces are marked with a '.', you can move to these spaces.
When moving make sure you put a space between each move.
e.g. I want to move from (5,6) to (4,7). I enter: '5,6 4,7'
e.g. I want to multi-jump from (5,6) to (3,4) to (1,2). I enter: '5,6 3,4 1,2'
For more in-depth instructions, view the README.md file.
If the keywords [ENTER] pops up, just press the enter key.
"""

TITLE = """
▗▄▄▄▄▄▄▄▄▄▄▄▖▗▄▖       ▗▄▖▗▄▄▄▄▄▄▄▄▄▄▄▖▗▄▄▄▄▄▄▄▄▄▄▄▖▗▄▖   ▗▄▖▗▄▄▄▄▄▄▄▄▄▄▄▖▗▄▄▄▄▄▄▄▄▄▄▄▖▗▄▄▄▄▄▄▄▄▄▄▄▖
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▗▟░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▛▀▀▀▀▀▀▀▀▀▘▐░▌       ▐░▌▐░▛▀▀▀▀▀▀▀▀▀▘▐░▛▀▀▀▀▀▀▀▀▀▘▐░▌ ▗▟░▛▘▐░▛▀▀▀▀▀▀▀▀▀▘▐░▛▀▀▀▀▀▀▀▜░▌▐░▛▀▀▀▀▀▀▀▀▀▘
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▗▟░▛▘ ▐░▌          ▐░▌       ▐░▌▐░▌
▐░▌          ▐░▙▄▄▄▄▄▄▄▟░▌▐░▙▄▄▄▄▄▄▄▄▄▖▐░▌          ▐░▙▟░▛▘  ▐░▙▄▄▄▄▄▄▄▄▄▖▐░▙▄▄▄▄▄▄▄▟░▌▐░▙▄▄▄▄▄▄▄▄▄▖
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░▌   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌          ▐░▛▀▀▀▀▀▀▀▜░▌▐░▛▀▀▀▀▀▀▀▀▀▘▐░▌          ▐░▛▜░▙▖  ▐░▛▀▀▀▀▀▀▀▀▀▘▐░▛▀▀▀▀▜░▛▀▀▘▝▀▀▀▀▀▀▀▀▀▜░▌
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▝▜░▙▖ ▐░▌          ▐░▌    ▝▜░▙▖           ▐░▌
▐░▙▄▄▄▄▄▄▄▄▄▖▐░▌       ▐░▌▐░▙▄▄▄▄▄▄▄▄▄▖▐░▙▄▄▄▄▄▄▄▄▄▖▐░▌ ▝▜░▙▖▐░▙▄▄▄▄▄▄▄▄▄▖▐░▌     ▝▜░▙▖▗▄▄▄▄▄▄▄▄▄▟░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▝▜░▌▐░░░░░░░░░░░▌▐░▌      ▝▜░▌▐░░░░░░░░░░░▌
▝▀▀▀▀▀▀▀▀▀▀▀▘▝▀▘       ▝▀▘▝▀▀▀▀▀▀▀▀▀▀▀▘▝▀▀▀▀▀▀▀▀▀▀▀▘▝▀▘   ▝▀▘▝▀▀▀▀▀▀▀▀▀▀▀▘▝▀▘       ▝▀▘▝▀▀▀▀▀▀▀▀▀▀▀▘"""
P1_PROMPT = "P1, what are your commands? (row,col row,col) \n> "
P2_PROMPT = "P2, what are your commands? (row,col row,col) \n> "
HEADER = "    0   1   2   3   4   5   6   7"
TOPROW = "  ┌───┬───┬───┬───┬───┬───┬───┬───┐"
MIDROW = "  ├───┼───┼───┼───┼───┼───┼───┼───┤"
FOOTER = "  └───┴───┴───┴───┴───┴───┴───┴───┘"

# Pre-defined Variables
board = [
[5, 2, 5, 2, 5, 2, 5, 2],
[2, 5, 2, 5, 2, 5, 2, 5],
[5, 2, 5, 2, 5, 2, 5, 2],
[0, 5, 0, 5, 0, 5, 0, 5],
[5, 0, 5, 0, 5, 0, 5, 0],
[1, 5, 1, 5, 1, 5, 1, 5],
[5, 1, 5, 1, 5, 1, 5, 1],
[1, 5, 1, 5, 1, 5, 1, 5]]

tempBoard = deepcopy(board) # Creates a dummy copy of board
possibleJumps = [] # Start at blank

# Functions
def intChecker(num):
  """Checks if the given value is castable as an integer"""
  try:
    int(num)
    return True
  except:
    return False


def pieceInSquare(player, pos):
  """Checks if a player's pieces are in the square"""
  row = int(pos[0]) # String slicing: e.g: 5,2 - row=5 | col=2
  col = int(pos[2])
  if (tempBoard[row][col] == player) or (tempBoard[row][col] == player+2):
    return True
  return False


def squareEmpty(pos):
  """Checks if the square is empty"""
  if intChecker(pos[0]) and intChecker(pos[2]):
    row = int(pos[0])
    col = int(pos[2])
    return (tempBoard[row][col] == 0)
  return False


def whatPiece(player, pos):
  """Checks what type of piece is in the square"""
  if intChecker(pos[0]) and intChecker(pos[2]):
    row = int(pos[0])
    col = int(pos[2])
    if tempBoard[row][col] == player:
      return "reg"
    elif tempBoard[row][col] == player+2:
      return "king"


def validRegMove(player, pos, new):
  """Move validation for reg pieces"""
  row = int(pos[0])
  col = int(pos[2])
  newRow = int(new[0])
  newCol = int(new[2])
  # Checks the 2 possible dirs based on the player
  if squareEmpty(new):
    if player == 1:
      if (newRow,newCol) == (row-1,col-1) or (newRow,newCol) == (row-1,col+1):
        return True
    elif player == 2:
      if (newRow,newCol) == (row+1,col-1) or (newRow,newCol) == (row+1,col+1):
        return True
  return False


def validKingMove(pos, new):
  """Move validation for king pieces"""
  row = int(pos[0])
  col = int(pos[2])
  newRow = int(new[0])
  newCol = int(new[2])
  # Checks the 4 possible dirs
  if squareEmpty(new):
    if (newRow,newCol) == (row-1,col-1) or (newRow,newCol) == (row-1,col+1) or (newRow,newCol) == (row+1,col+1) or (newRow,newCol) == (row+1,col-1):
      return True
  return False


def whosePiece(pos):
  """Checks what piece is in the square"""
  return (tempBoard[int(pos[0])][int(pos[2])])


def squareExists(pos):
  """Checks if the square exists"""
  if intChecker(pos[0]) and intChecker(pos[2]):
    row = int(pos[0])
    col = int(pos[2])
    if row < 8 and row >= 0 and col < 8 and col >= 0:
      return True
  return False


def regMove(player, pos, new):
  """Move basis for reg pieces"""
  row = int(pos[0])
  col = int(pos[2])
  newRow = int(new[0])
  newCol = int(new[2])
  # Does this pos have this piece and does this pos exist? 
  if pieceInSquare(player, pos) and squareExists(new):
    tempBoard[row][col] = 0
    tempBoard[newRow][newCol] = player


def kingMove(player, pos, new):
  """Move basis for king pieces"""
  row = int(pos[0])
  col = int(pos[2])
  newRow = int(new[0])
  newCol = int(new[2])
  # Does this pos have this piece and does this pos exist? 
  if pieceInSquare(player, pos) and squareExists(new):
    tempBoard[row][col] = 0
    tempBoard[newRow][newCol] = player


def validJump(player, pos, new):
  """Jump validation for all pieces"""
  possibleSpaces = []
  # Is it P1 or a king?
  if player == 1 or player > 2:
    possibleSpaces.append(f"{int(pos[0])-1},{int(pos[2])-1}")
    possibleSpaces.append(f"{int(pos[0])-1},{int(pos[2])+1}")
    # Does pos exist?
    available = [i for i in possibleSpaces if squareExists(i)]

  # Is it P2 or a king?
  if player == 2 or player > 2:
    possibleSpaces.append(f"{int(pos[0])+1},{int(pos[2])-1}")
    possibleSpaces.append(f"{int(pos[0])+1},{int(pos[2])+1}")
    available = [i for i in possibleSpaces if squareExists(i)]
  # Checks if king piece because kings can move in all 4 dirs
  if player == 1 or player == 3:
    for item in available:
      # Is the piece we're jumping over an enemy piece?
      if whosePiece(item) == 2 or whosePiece(item) == 4:
        if squareEmpty(new):
          # Get pos inbetween the jump's position
          midRow = int((int(pos[0]) + int(new[0]))/2)
          midCol = int((int(pos[2]) + int(new[2]))/2)
          # Enemy piece's pos in same direction as we're going?
          if item == f"{midRow},{midCol}":
            return True

  elif player == 2 or player == 4:
    for item in available:
      if whosePiece(item) == 1 or whosePiece(item) == 3:
        if squareEmpty(new):
          midRow = int((int(pos[0]) + int(new[0]))/2)
          midCol = int((int(pos[2]) + int(new[2]))/2)
          if item == f"{midRow},{midCol}":
            return True
  return False


def jump(player, pos, new):
  """Jump basis for all pieces"""
  row = int(pos[0])
  col = int(pos[2])
  newRow = int(new[0])
  newCol = int(new[2])
  midRow = int((row + newRow)/2)
  midCol = int((col + newCol)/2)
  
  tempBoard[midRow][midCol] = 0
  tempBoard[newRow][newCol] = tempBoard[row][col]
  tempBoard[row][col] = 0


def kingPiece(player, new):
  """Kings a piece"""
  tempBoard[int(new[0])][int(new[2])] = player+2


def validMove(player, selected, move):
  """Main move validator for all pieces"""
  if whatPiece(player, selected) == "reg":
    if validJump(player, selected, move):
      return True
    
    elif validRegMove(player, selected, move):
      return True
    
    elif int(move[0]) == 0 or int(move[0]) == 7:
      return True

  elif whatPiece(player, selected) == "king":
    if validKingMove(selected, move):
      return True
  return False

def checkPossibleJumps(board, player, possibleJumps):
  """Checks if any of the player's pieces can jump"""
  potentials = [] # List that stores possible moves
  row = col = 0
  for list in board:
    for i in list:
      if i == player or i == player+2:
        selected = f"{row},{col}"
        pieceType = whosePiece(selected)
        if pieceType == 1 or pieceType > 2:
          potentials.append(f"{int(selected[0])-2},{int(selected[2])-2}")
          potentials.append(f"{int(selected[0])-2},{int(selected[2])+2}")
        if pieceType == 2 or pieceType > 2:
          potentials.append(f"{int(selected[0])+2},{int(selected[2])-2}")
          potentials.append(f"{int(selected[0])+2},{int(selected[2])+2}")
        for j in range(len(potentials)):
          if squareExists(potentials[j]):
            if validJump(pieceType, selected, potentials[j]):
              possibleJumps.append(f"{selected} {potentials[j]}")
        potentials = []
      col += 1
    row += 1
    col = 0


def updateBoard(board, turn):
  """Updates the board printed to the >_ Console"""
  newBoard = []
  odd = False
  row = 0
  for list in board:
    newBoard.append([])
    for i in list:
      if i == 0:
        newBoard[row].append("│ . │")
      if i == 1:
        newBoard[row].append("│ x │")
      if i == 2:
        newBoard[row].append("│ o │")
      if i == 3:
        newBoard[row].append("│ X │")
      if i == 4:
        newBoard[row].append("│ O │")
    row += 1

  for i in range(8):
    newBoard[i] = "   ".join(newBoard[i])
  clear()
  print(f"It is P{turn}'s turn\n")
  print(f"{HEADER}\n{TOPROW}")

  for i in range(8):
    print(f"{i} {newBoard[i]}   │") if odd else print(f"{i} │   {newBoard[i]}")
    if i != 7:
      print(MIDROW)
    odd = not odd # Make odd the opposite value in 1 line
  print(FOOTER)


def p1Turn(board, undoBoard=[]):
  """Player 1's Turn Function"""
  global tempBoard, possibleJumps
  if undoBoard != []:
    tempBoard = deepcopy(undoBoard)
  undone = False
  moves = list(map(str, input(P1_PROMPT).split(" ")))
  if len(moves) > 2:
    for i in range(1, len(moves)+1):
      if i < len(moves):
        selected = moves[i-1]
        move = moves[i]
        try:
          if intChecker(move[0]) and intChecker(move[2]) and intChecker(selected[0]) and intChecker(selected[2]):
            if len(move) == 3 and len(selected) == 3:
              pass
            else:
              print("That's NOT a valid move. Try again.")
              print(f"You cannot move a piece from {selected} to {move}.")
              moves = []
              p1Turn(board, undoBoard=deepcopy(board))
              undone = True
              break
        except:
          print("That's NOT a valid move. Try again.")
          print(f"You cannot move a piece from {selected} to {move}.")
          moves = []
          p1Turn(board, undoBoard=deepcopy(board))
          undone = True
          break
        if whatPiece(1, selected) == "reg":
          if not validJump(1, selected, move):
            print("That's NOT a valid move. Try again.")
            print(f"You cannot move a piece from {selected} to {move}.")
            moves = []
            p1Turn(board, undoBoard=deepcopy(board))
            undone = True
            break
          else:
            if not undone:
              jump(1, selected, move)

        elif whatPiece(1, selected) == "king":
          if not validJump(3, selected, move):
            print("That's NOT a valid move. Try again.")
            print(f"You cannot move a piece from {selected} to {move}.")
            moves = []
            p1Turn(board, undoBoard=deepcopy(board))
            undone = True
            break
          else:
            if not undone:
              jump(3, selected, move)

      elif i == len(moves):
        if not undone:
          checkJump1 = f"{int(move[0])-2},{int(move[2])-2}"
          checkJump2 = f"{int(move[0])-2},{int(move[2])+2}"
          if whatPiece(1, move) == "reg":
            if validJump(1, move, checkJump1):
              print(f"You can jump from {move} to {checkJump1}.")
  
            if validJump(1, move, checkJump2):
              print(f"You can jump from {move} to {checkJump2}.")
  
            if validJump(1, move, checkJump1) or validJump(1, move, checkJump2):
              input("> [ENTER]")
              moves = []
              p1Turn(board, undoBoard=deepcopy(board))
              undone = True
  
          elif whatPiece(1, move) == "king":
            checkJump3 = f"{int(move[0])+2},{int(move[2])-2}"
            checkJump4 = f"{int(move[0])+2},{int(move[2])+2}"
            if validJump(3, move, checkJump1):
              print(f"You can jump from {move} to {checkJump1}.")
  
            if validJump(3, move, checkJump2):
              print(f"You can jump from {move} to {checkJump2}.")
  
            if validJump(3, move, checkJump3):
              print(f"You can jump from {move} to {checkJump3}.")
  
            if validJump(3, move, checkJump4):
              print(f"You can jump from {move} to {checkJump4}.")
  
            if validJump(3, move, checkJump1) or validJump(3, move, checkJump2) or validJump(3, move, checkJump3) or validJump(3, move, checkJump4):
              input("> [ENTER] ")
              moves = []
              p1Turn(board, undoBoard=deepcopy(board))
              undone = True
        break
# If you stay in loop, you will exceed array's max index val.

  elif len(moves) == 2:
    selected = moves[0]
    move = moves[1]
    try:
      if intChecker(move[0]) and intChecker(move[2]) and intChecker(selected[0]) and intChecker(selected[2]):
        if len(move) == 3 and len(selected) == 3:
          pass # Extra check for if the move is possible
        else:
          print("That's NOT a valid move. Try again.")
          print(f"You cannot move a piece from {selected} to {move}.")
          moves = []
          p1Turn(board, undoBoard=deepcopy(board))
          undone = True
    except:
      print("That's NOT a valid move. Try again.")
      print(f"You cannot move a piece from {selected} to {move}.")
      moves = []
      p1Turn(board, undoBoard=deepcopy(board))
      undone = True
    if possibleJumps != []:
      for i in range(len(possibleJumps)+1):
        if i < len(possibleJumps):
          jumpNum = possibleJumps[i] # Dunno why this fixed a bug
          jumpMove = f"{selected} {move}"
          if jumpMove == jumpNum:
            break
        elif i == len(possibleJumps):
          print("At least one of your pieces can jump.")
          input("> [ENTER]")
          moves = []
          p1Turn(board, undoBoard=deepcopy(board))
          undone = True
          break

    if whatPiece(1, selected) == "reg":
      if not validMove(1, selected, move):
        print("That's NOT a valid move! Try again.")
        print(f"You cannot move a piece from {selected} to {move}.")
        moves = []
        p1Turn(board, undoBoard=deepcopy(board))
        undone = True
      else:
        if not undone:
          if validRegMove(1, selected, move):
            regMove(1, selected, move)
          elif validJump(1, selected, move):
            jump(1, selected, move)

    elif whatPiece(1, selected) == "king":
      if not validMove(3, selected, move):
        print("That's NOT a valid move! Try again.")
        print(f"You cannot move a piece from {selected} to {move}.")
        moves = []
        p1Turn(board, undoBoard=deepcopy(board))
        undone = True
      else:
        if not undone:
          if validKingMove(selected, move):
            kingMove(3, selected, move)
          elif validJump(3, selected, move):
            jump(3, selected, move)

    else:
      if not undone:
        print("That's NOT a valid move! Try again.")
        print(f"You cannot move a piece from {selected} to {move}.")
        moves = []
        p1Turn(board, undoBoard=deepcopy(board))
        undone = True

  else:
    print("You can't pass your turn in checkers. Try again.")
    moves = []
    p1Turn(board)
    undone = True

  if not undone:
    if whatPiece(1, move) == "reg":
      if int(move[0]) == 0:
        kingPiece(1, move)


def p2Turn(board, undoBoard=[]):
  """Player 2's Turn Function"""
  global tempBoard, possibleJumps
  if undoBoard != []:
    tempBoard = deepcopy(undoBoard)
  undone = False
  moves = list(map(str, input(P2_PROMPT).split(" ")))
  if len(moves) > 2:
    for i in range(1, len(moves)+1):
      if i < len(moves):
        selected = moves[i-1]
        move = moves[i]
        try:
          if intChecker(move[0]) and intChecker(move[2]) and intChecker(selected[0]) and intChecker(selected[2]):
            if len(move) == 3 and len(selected) == 3:
              pass
            else:
              print("That's NOT a valid move. Try again.")
              print(f"You cannot move a piece from {selected} to {move}.")
              moves = []
              p2Turn(board, undoBoard=deepcopy(board))
              undone = True
              break
        except:
          print("That's NOT a valid move. Try again.")
          print(f"You cannot move a piece from {selected} to {move}.")
          moves = []
          p2Turn(board, undoBoard=deepcopy(board))
          undone = True
          break
        if whatPiece(2, selected) == "reg":
          if not validJump(2, selected, move):
            print("That's NOT a valid move. Try again.")
            print(f"You cannot move a piece from {selected} to {move}.")
            moves = []
            p2Turn(board, undoBoard=deepcopy(board))
            undone = True
            break
          else:
            jump(2, selected, move)

        elif whatPiece(2, selected) == "king":
          if not validJump(4, selected, move):
            print("That's NOT a valid move. Try again.")
            print(f"You cannot move a piece from {selected} to {move}.")
            moves = []
            p2Turn(board, undoBoard=deepcopy(board))
            undone = True
            break
          else:
            jump(4, selected, move)

      elif i == len(moves):
        if not undone:
          checkJump1 = f"{int(move[0])+2},{int(move[2])-2}"
          checkJump2 = f"{int(move[0])+2},{int(move[2])+2}"
          if whatPiece(2, selected) == "reg":
            if validJump(2, move, checkJump1):
              print(f"You can jump from {move} to {checkJump1}.")
  
            if validJump(2, move, checkJump2):
              print(f"You can jump from {move} to {checkJump2}.")
  
            if validJump(2, move, checkJump1) or validJump(2, move, checkJump2):
              input("> [ENTER]")
              moves = []
              p2Turn(board, undoBoard=deepcopy(board))
              undone = True
  
          elif whatPiece(2, move) == "king":
            checkJump3 = f"{int(move[0])-2},{int(move[2])-2}"
            checkJump4 = f"{int(move[0])-2},{int(move[2])+2}"
            if validJump(4, move, checkJump1):
              print(f"You can jump from {move} to {checkJump1}.")
  
            if validJump(4, move, checkJump2):
              print(f"You can jump from {move} to {checkJump2}.")
  
            if validJump(4, move, checkJump3):
              print(f"You can jump from {move} to {checkJump3}.")
  
            if validJump(4, move, checkJump4):
              print(f"You can jump from {move} to {checkJump4}.")
  
            if validJump(4, move, checkJump1) or validJump(4, move, checkJump2) or validJump(4, move, checkJump3) or validJump(4, move, checkJump4):
              input("> [ENTER] ")
              moves = []
              p2Turn(board, undoBoard=deepcopy(board))
              undone = True
        break

  elif len(moves) == 2:
    selected = moves[0]
    move = moves[1]
    try:
      if intChecker(move[0]) and intChecker(move[2]) and intChecker(selected[0]) and intChecker(selected[2]):
        if len(move) == 3 and len(selected) == 3:
          pass
        else:
          print("That's NOT a valid move. Try again.")
          print(f"You cannot move a piece from {selected} to {move}.")
          moves = []
          p2Turn(board, undoBoard=deepcopy(board))
          undone = True
    except:
      print("That's NOT a valid move. Try again.")
      print(f"You cannot move a piece from {selected} to {move}.")
      moves = []
      p2Turn(board, undoBoard=deepcopy(board))
      undone = True
    if possibleJumps != []:
      for i in range(len(possibleJumps)+1):
        if i < len(possibleJumps):
          jumpNum = possibleJumps[i] # Dunno why this fixed a bug
          jumpMove = f"{selected} {move}"
          if jumpMove == jumpNum:
            break
        elif i == len(possibleJumps):
          print("At least one of your pieces can jump.")
          input("> [ENTER]")
          moves = []
          p2Turn(board)
          undone = True
          break

    if whatPiece(2, selected) == "reg":
      if not validMove(2, selected, move):
        print("That's NOT a valid move! Try again.")
        print(f"You cannot move a piece from {selected} to {move}.")
        moves = []
        p2Turn(board, undoBoard=deepcopy(board))
        undone = True
      else:
        if validRegMove(2, selected, move):
          regMove(2, selected, move)
        elif validJump(2, selected, move):
          jump(2, selected, move)

    elif whatPiece(2, selected) == "king":
      if not validMove(4, selected, move):
        print("That's NOT a valid move! Try again.")
        print(f"You cannot move a piece from {selected} to {move}.")
        moves = []
        p2Turn(board, undoBaord=board)
        undone = True
      else:
        if validKingMove(selected, move):
          kingMove(4, selected, move)
        elif validJump(4, selected, move):
          jump(4, selected, move)
    else:
      print("That's NOT a valid move! Try again.")
      print("You cannot move an empty square.")
      moves = []
      p2Turn(board, undoBoard=deepcopy(board))
      undone = True
  else:
    if not undone:
      print("You can't pass your turn in checkers. Try again.")
      moves = []
      p2Turn(board, undoBoard=deepcopy(board))
      undone = True

  if not undone:
    if whatPiece(2, move) == "reg":
      if int(move[0]) == 7:
        kingPiece(2, move)


# Main Program
print("Welcome to:")
print(Fore.CYAN + "")
print(TITLE)
print("" + Fore.RESET)

playing = True
print(INTRO)
input("> [ENTER]")
updateBoard(board, 1)

while playing:
  # END GAME
  data1 = data2 = []
  for i in range(0, 8):
    data1.append((1 in board[i]) or (3 in board[i]))
    data2.append((2 in board[i]) or (4 in board[i]))

  if (True in data1) and (True in data2):
    playing = True

  elif (True in data1) and (False in data2):
    print("Player 1 has won the game!")
    input("> ")
    playing = False

  elif (False in data2) and (True in data2):
    print("Player 2 has won the game!")
    input("> ")
    playing = False

  # P1 and P2
  possibleJumps = []
  checkPossibleJumps(board, 1, possibleJumps)
  p1Turn(board)
  board = deepcopy(tempBoard)

  updateBoard(board, 2)
  possibleJumps = []
  checkPossibleJumps(board, 2, possibleJumps)
  p2Turn(board)
  board = deepcopy(tempBoard)
  updateBoard(board, 1)

print("Thanks for playing, bye!") # END
