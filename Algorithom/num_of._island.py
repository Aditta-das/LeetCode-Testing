class Solution(object):
		def numIslands(self, grid):
			num_island = 0
			for r in range(len(grid)):
				for c in range(len(grid[r])):
					if grid[r][c] == "1":
						self.dfs(grid, r, c)
						num_island += 1
			return num_island
		
		def dfs(self, grid, r, c):
			grid[r][c] = "0"
			lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
			for row, col in lst:
				if row >=0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == "1":
					self.dfs(grid, row, col)
	



grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0"],
	["0","0","0","0","0"]
]
a = Solution()
print(a.numIslands(grid))