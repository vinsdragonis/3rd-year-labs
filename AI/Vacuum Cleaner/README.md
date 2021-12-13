# Vacuum Cleaner AI

## Objective
Given M x N grid(floor) create an agent that moves around the grid until the entire grid is clean

- Move the agent anyway you see fit until the floor is clean, **Zig-Zag** in my implementation
- Agent can start at any tile on the floor, given as input to the program

## Notation
The floor is represented by a M x N grid where **1** represents a _dirty_ tile and **0** represents a _clean_ tile
```
floor = [[1, 0, 0, 0], 
         [0, 1, 0, 1],
         [1, 0, 1, 1]]
```

## Algorithm
```
function CLEAN(floor, startRow, startCol):
    goRight = True
    i = startRow, j = startCol
    while the floor is not clean:
        currentTile = floor[i][j]
        if currentTile is dirty, clean it
        choose next cell to move to:
            if in last column and goRight
                go down 
                toggle goRight 
            else if in first column and not goRight
                go down 
                toggle goRight          
            else
                go right if goRight else go left
        move to next cell (update coordinates)
```

## Utility Functions
1. `print_floor(floor)` - Prints the floor at an instance of time
2. `notClean(floor)` - Check if any tile is dirty, return true if so, else false
