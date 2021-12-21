# Knowledge-Base Entailment

## Objective

Given a knowledge-base using **propositional logic**, prove the given query using **resolution**.

## Notation

    variables = [p, q, r]

## Logic

The successive moves are computed by **brute force** technique

    function compMove():
        if board has empty corners:
            set empty corner to O
            return move

        if board has empty center:
            set middle to O
            return move
            
        if board has empty mid slot:
            set empty mid slot to O
            return move
            
## Utility Functions

1. `compMove()` - Checks for an empty slot and places a **0** accordingly
2. `isWinner(board, letter)` - Checks for **three** consecutive **O(s)** or **X(s)** *vertically, horizontally, or diagonally*
3. `playerMove()` - Validates input position entered by the *player* and places a **X** if it is empty
4. `drawBoard(board)` - Draws the board and prints the values in each postion
5. `inputLetter(letter, position)` - Sets the value for the given position on the board
6. `freespace(position)` - Checks if the given position is empty and returns the same to `playerMove()`
7. `selectRandom(list)` - Computes the length of the given list and selects a random position within the given range
8. `isBoardFull(board)` - Checks if all positions are used up
9. `main()` - The main function where all functions are put together
