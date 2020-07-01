class Solution(object):
    def bfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
            return 
        
        if grid[x][y] == 1:
            grid[x][y] = 0
            self.bfs(grid, x-1, y)
            self.bfs(grid, x+1, y)
            self.bfs(grid, x, y-1)
            self.bfs(grid, x, y+1)

    def printGrid(self, grid):
        for i in grid:
            print(i)
        print("======================")


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        self.printGrid(grid)
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    self.bfs(grid, x,y)
                    self.printGrid(grid)
                    count += 1
        return count



grid = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0],
    ]
a = Solution()
print(a.numIslands(grid))
            
            