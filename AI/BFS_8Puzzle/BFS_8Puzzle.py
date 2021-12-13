def print_grid(matrix):
    state = matrix.copy()
    state[state.index(-1)] = "_"
    print(
        f"""
        {state[0]} {state[1]} {state[2]}
        {state[3]} {state[4]} {state[5]}
        {state[6]} {state[7]} {state[8]}
        """
    )


def gen(state, b, d):
    x = []
    for i in d:
        temp = state.copy()
        if i == "up":
            temp[b-3], temp[b] = temp[b], temp[b-3]
        elif i == "down":
            temp[b+3], temp[b] = temp[b], temp[b+3]
        elif i == "right":
            temp[b+1], temp[b] = temp[b], temp[b+1]
        elif i == "left":
            temp[b-1], temp[b] = temp[b], temp[b-1]
        x.append(temp)
    return x


def bfs(src, target):
    frontier = [src]
    visited_states = set()
    while len(frontier):
        state = frontier.pop(0)
        print_grid(state)
        visited_states.add(tuple(state))
        if(state == target):
            print("Success")
            return
        else:
            for move in possible_moves(state, visited_states):
                if move not in frontier:
                    frontier.append(move)
    print("Fail")


def possible_moves(state, visited_states):
    b = state.index(-1)
    d = []
    if b not in (0, 1, 2):
        d.append("up")
    if b not in (6, 7, 8):
        d.append("down")
    if b not in (0, 3, 6):
        d.append("left")
    if b not in (2, 5, 8):
        d.append("right")
    return [move for move in gen(state, b, d) if tuple(move) not in visited_states]


src = [1, 2, 5, -1, 3, 4, 6, 7, 8]
target = [-1, 1, 2, 3, 4, 5, 6, 7, 8]


bfs(src, target)
