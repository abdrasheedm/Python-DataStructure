"""
Solve the below problem: You’re given a two-dimensional array (a matrix) of potentially unequal height & width containing only 0’s & 1’s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1’s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1’s forming a river determine its size.
Note that a river can twist. In other words, it doesn’t have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.
Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don’t need to be in any particular order.

"""


def dfs(row, col, visited, matrix):
    if row not in range(len(matrix)) or col not in range(len(matrix[0])) or matrix[row][col] == 0 or (row, col) in visited: return 0
    visited.add((row, col))
    size = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        size += dfs(row+dx, col+dy, visited, matrix)
    return 1 + size


def riverSizes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    ans = []

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited and matrix[row][col] == 1:
                size = dfs(row, col, visited, matrix)
                ans.append(size)

    return ans

matrix =  [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
print(riverSizes(matrix))
