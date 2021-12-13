def notClean(floor):
    for row in floor:
        if 1 in row:
            return True
    return False


def clean(floor, i, j):
    goRight = True

    while notClean(floor):
        # Print Floor
        print_floor(floor, i, j)
        # Clean
        if floor[i][j]:
            floor[i][j] = 0
        # Decide Direction and Move (Zig-Zag)
        if j == len(floor[i])-1 and goRight:
            i, right = (i + 1) % len(floor), False
            continue
        elif j == 0 and not goRight:
            i, right = (i + 1) % len(floor), True
            continue
        else:
            j = j + 1 if goRight else j - 1

    # Cleaned Floor
    print_floor(floor, -1, -1)


def print_floor(floor, curr_row, curr_col):
    for row in range(len(floor)):
        for col in range(len(floor[row])):
            if (curr_row, curr_col) == (row, col):
                print(" >", floor[row][col], "< ", end='', sep='')
            else:
                print("  ", floor[row][col], "  ", end='', sep='')
        print()
    print()


floor = [[1, 0],
        [0, 1]]

clean(floor, 0, 0)
