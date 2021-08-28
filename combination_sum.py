class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(candidates)

        def backTrack(idx, cur, target):
            if target == 0:
                res.append(list(cur))
                return
            
            elif target < 0:
                return 

            for i in range(idx, n):
                cur.append(candidates[i])
                backTrack(i, cur, target - candidates[i])
                cur.pop()

        backTrack(0, [], target)
        return res

candidates = [2,3,6,7]
target = 7
a = Solution()
print(a.combinationSum(candidates, target))