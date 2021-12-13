# 8 Puzzle Iterative Deepening Depth First Search

## Objective

Given a **3 x 3** grid, the aim is to create an agent to *solve the puzzle* by moving the tiles **vertically or horizontally** until it reaches the **goal state** using
**IDDFS algorithm**.

## Notation

The grid is represented as a **3 x 3 matrix**, where there are 8 tiles numbered from **1 to 8** and a **blank space** represented by **_**

    example_grid = [[ 1, 2, 3 ],
                    [ 4, 5, 6 ],
                    [ 7, 8, _ ]]

## Logic

All possible moves are computed by **IDDFS** technique, and we search **if the target state is *reachable or not***.

### DFS

    function dfs(src, target, limit, visited_states):
		if src is target:
			return True
		if limit <= 0:
			return False
			
		visited_states.append(src)
		moves = possible_moves(src, visited_states)
		
		for move in moves:
			if dfs(move, target, limit-1, visited_states):
				return True
		return False
	
### IDDFS

	function iddfs(src, target, depth):
		for i in range(depth):
			visited_states = []
			if dfs(src, target, i+1, visited_states):
				return True
		return False
            
## Utility Functions

1. `dfs(src, target, limit, visited_states)` - Searches if **current state** is **goal state** or not, and appends the nodes to the visited array
2. `gen(state, move, blank):` - Generates a **new state** for that sequence
3. `possible_moves(state, visited_states)` - Checks for **all possible moves**
4. `iddfs(src, target, depth)` - Iterates till the **limit is reached** and searches through the grid, or if **goal state is reached** and prints if the given state is
**reachable or not**
