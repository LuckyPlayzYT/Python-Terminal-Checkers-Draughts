### IntChecker
"Checks if the given value is castable as an integer"
#### Required Arguments:
`num`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### PieceInSquare
"Checks if one of the player's pieces are in the square"
#### Required Arguments:
`player`, `Pos`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### SquareEmpty
"Checks if the square is empty"
#### Required Arguments:
`pos`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### whatPiece
"Checks what type of piece is in the square"
#### Required Arguments:
`player`, `pos`

#### Optional Arguments:
`None`

#### Return Values:
`"reg"`/`"king"`

#

### validRegMove
"Move validation for reg pieces"
#### Required Arguments:
`player`, `pos`, `new`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### validKingMove
"Move validation for king pieces"
#### Required Arguments:
`pos`, `new`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### WhosePiece
"Checks what piece is in the square"
#### Required Arguments:
`pos`

#### Optional Arguments:
`None`

#### Return Values:
`pos`'s value in `tempBoard`

#

### SquareExists
"Checks if the square exists"
#### Required Arguments:
`num`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### RegMove
"Move basis for reg pieces"
#### Required Arguments:
`player`, `pos`, `new`

#### Optional Arguments:
`None`

#### Return Values:
`None`

#

### kingMove
"Move basis for king pieces"
#### Required Arguments:
`player`, `pos`, `new`

#### Optional Arguments:
`None`

#### Return Values:
`None`

#

### validJump
"Jump validation for all pieces"
#### Required Arguments:
`player`, `pos`, `new`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### jump
"Jump basis for all pieces"
#### Required Arguments:
`player`, `pos`, `new`

#### Optional Arguments:
`None`

#### Return Values:
`None`

#

### kingPiece
"Kings a piece"
#### Required Arguments:
`player`, `new`

#### Optional Arguments:
`None`

#### Return Values:
`None`

#

### validMove
"Main move validator for all pieces"
#### Required Arguments:
`player`, `selected`, `move`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### checkPossibleJumps
"Checks if any of the player's pieces can jump"
#### Required Arguments:
`board`, `player`, `possibleJumps`

#### Optional Arguments:
`None`

#### Return Values:
`True`/`False`

#

### updateBoard
"Updates the board printed to the >_ Console"
#### Required Arguments:
`board`, `turn`

#### Optional Arguments:
`None`

#### Return Values:
`None`

#

### P1Turn
"Player 1's Turn Function"
#### Required Arguments:
`board`

#### Optional Arguments:
`undoBoard=[]`

#### Return Values:
`None`

#

### P2Turn
"Player 2's Turn Function"
#### Required Arguments:
`board`

#### Optional Arguments:
`undoBoard=[]`

#### Return Values:
`None`
