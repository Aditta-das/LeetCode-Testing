class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        # print(candidates)
        res =[]
        n = len(candidates)
        def backtrack(target, idx, cur):
            if target == 0:
                res.append(list(cur))
                return 
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i -1]:
                    continue
                pick = candidates[i]
                if target - pick < 0:
                    break
                cur.append(pick)
                backtrack(target-pick, i+1, cur)
                cur.pop()
    
        backtrack(target, 0, [])
        
        return res

candidates = [10,1,2,7,6,1,5]
target = 9
a = Solution()
print(a.combinationSum2(candidates, target))