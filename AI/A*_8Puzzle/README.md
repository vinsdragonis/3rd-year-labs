# 8 Puzzle A* Search Algorithm

## Objective

Given a **3 x 3** grid, the aim is to create an agent to *solve the puzzle* by moving the tiles **vertically or horizontally** until it reaches the **goal state** using
**A*** **algorithm**.

## Notation

The grid is represented as a **3 x 3 matrix**, where there are 8 tiles numbered from **1 to 8** and a **blank space** represented by **_**

    example_grid = [[ 1, 2, 3 ],
                    [ 4, 5, 6 ],
                    [ 7, 8, _ ]]

## Logic

All possible moves are computed by **A*** technique, and the astar function solves the puzzle by moving the blank space up, down, left, or right until the goal state has been
reached.

    function astar(src, target):
		states = src
		g = 0
		visited_states = []
		
		while len(states):
			moves = []
			for state in states:
				visited_states.add(state)
				if state == target:
					return True
				if move not in moves:
					moves += [move for move in possible_moves(state, visited_states)]
			costs = [g + h(move, target) for move in moves]
			for i in range(len(moves)):
				if costs[i] is min(costs):
					states = [moves[i]]
			g += 1
		print False
            
## Utility Functions

1. `h(state, target)` - Compute **Manhattan distance**
2. `astar(src, target)` - Computes the **moves made** and checks if the puzzle **can be solved** or **not**
3. `possible_moves(state, visited_states)` - Checks for **all possible moves**
4. `print_grid(src)` - Draws the **grid** and prints the values in **each postion**
5. `gen(state, direction, b)` - Generate state
