# 8 Puzzle Breadth First Search

## Objective

Given a **3 x 3** grid, the aim is to create an agent to *solve the puzzle* by moving the tiles **vertically or horizontally** until it reaches the **goal state** using
**BFS algorithm**.

## Notation

The grid is represented as a **3 x 3 matrix**, where there are 8 tiles numbered from **1 to 8** and a **blank space** represented by **_**

    example_grid = [[ 1, 2, 3 ],
                    [ 4, 5, 6 ],
                    [ 7, 8, _ ]]

## Logic

All possible moves are computed by **BFS** technique, and the search function checks breadth-wise which is the most suitable move

    function bfs(src, target):
        frontier = src
        
        while frontier.length:
            state = frontier.pop[0]
            visited_states.add(state)
            
            if state is target:
                print("Success")
                return
            else:
                for move in possible_moves(state, visited_states):
                    if move is not in frontier:
                        frontier.append(move)
        print("Unsuccessful")
            
## Utility Functions

1. `bfs(src, target)` - Checks if **current state** is **goal state** or not, and appends the nodes to the visited array
2. `gen(state, b, d)` - Generates a **new state** for that sequence
3. `possible_moves(state, visited_states)` - Checks for **all possible moves**
4. `print_grid(matrix)` - Draws the **grid** and prints the values in **each postion**
