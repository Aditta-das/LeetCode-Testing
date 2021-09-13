class Solution(object):
    def totalNQueens(self, n):
    	col = set()
    	posDiag = set()
    	negDiag = set()
    	res = []
    	board = [["."] * n for i in range(n)]
    	def backTrack(r):
    		if r == n:
    			board_copy = ["".join(row) for row in board]
    			res.append(board_copy)
    			return 
    		for c in range(n):
    			if c in col or (r + c) in posDiag or (r - c) in negDiag:
    				continue

    			col.add(c)
    			posDiag.add(r+c)
    			negDiag.add(r-c)
    			board[r][c] = "Q"

    			backTrack(r+1)

    			col.remove(c)
    			posDiag.remove(r+c)
    			negDiag.remove(r-c)
    			board[r][c] = "."

    	backTrack(0)
    	return len(res)  

n = 4
a = Solution()
print(a.totalNQueens(n))