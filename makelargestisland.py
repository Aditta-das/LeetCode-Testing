class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        b = [i for j in grid for i in j]
        count = {}
        for a in b:
            if not a in count:
                count[a] = 1
            else:
                count[a] += 1
                if a > 0:
                    print(a)        



grid = [[1,1],[1,0]]
a = Solution()
print(a.largestIsland(grid))