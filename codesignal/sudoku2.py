def sudoku2(grid):
  N = len(grid)
  # rows
  rows = set()
  columns = set()
  subgrid = set()
  for i in range(N):
    for j in range(N):
      rowV = grid[i][j]
      colV = grid[j][i]
      subV = grid[3* int(i*3 / 9) + int(j / 3)][(i*3 % 9) + (j % 3) ]
      if rowV != ".":
        if rowV not in rows:
          rows.add(rowV)
        else:
          return False
      if colV != ".":
        if colV not in columns:
          columns.add(colV)
        else:
          return False
      if subV != ".":
        if subV not in subgrid:
          subgrid.add(subV)
        else:
          return False
      
    rows = set()
    columns = set()
    subgrid = set()
  return True

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
print(sudoku2(grid))