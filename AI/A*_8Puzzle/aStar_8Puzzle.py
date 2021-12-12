import time
import colorama
from colorama import Fore, Style

# 8 Puzzle's problem using A* search with manhattan distance

class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_chid(self):
        x, y = self.find(self.data, '_')
        val = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for i in val:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                children.append(child_node)
        return children

    def find(self, puz, x):
        for i, row in enumerate(puz):
            for j, col in enumerate(row):
                if col == x:
                    return i, j

    def shuffle(self, puz, x, y, xf, yf):
        if(xf >= 0 and xf < len(puz) and yf >= 0 and yf < len(puz)):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[xf][yf]
            temp_puz[xf][yf] = puz[x][y]
            temp_puz[x][y] = temp
            return temp_puz
        else:
            return None

    def copy(self, puz):
        temp = []
        for i in puz:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        inpMatrix = []
        for i in range(0, self.n):
            temp = input().split(" ")
            inpMatrix.append(temp)
        return inpMatrix

    def f(self, start, goal):
        return self.h(start.data, goal)+start.level

    def h(self, start, goal):
        t = 0
        for i, row in enumerate(start):
            for j, col in enumerate(row):
                if(col != goal[i][j] and col != '_'):
                    t += 1
        return t

    def printMat(self, cur, count):

        print("\033c", end="")
        print(Fore.GREEN + "8-puzzle Problem using Heuristic Search and Manhattan distance\n" + Fore.RESET)
        for i in cur.data:
            for j in i:
                if j == '_':
                    print(Fore.CYAN + '█' + Fore.RESET, end=' ')
                else:
                    print(j, end=" ")
            print("")
        print("\nTotal moves : " + Fore.YELLOW +
              str(count) + Fore.RESET + '\n')

    def process(self):
        print("Enter the starting state matrix ")
        start = self.accept()
        print("Enter the goal state matrix ")
        goal = self.accept()
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)
        moves = 0
        while(True):
            cur = self.open[0]
            self.printMat(cur, moves)

            if(self.h(cur.data, goal) == 0):
                break

            for i in cur.generate_chid():
                i.fval = self.f(i, goal)
                self.open.append(i)

            self.closed.append(cur)
            del self.open[0]

            self.open.sort(key=lambda x: x.fval, reverse=False)
            moves += 1
            time.sleep(1)

puz = Puzzle(3)
puz.process()
