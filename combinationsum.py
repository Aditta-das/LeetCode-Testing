class Solution(object):
    def combinationSum(self, candidates, target):
        for i, a in enumerate(candidates):
            if target == a:
                direct_candidate = [a]
                candidates.pop(i)
            # else:
                l, r = 0, len(candidates) - 1
                while l < r:
                    sums = candidates[l] + candidates[r]
                    if sums < target:
                        r -= 1
                    return sum
        # return candidates, direct_candidate
            


candidates = [2,3,6,7]
target = 7
a = Solution()
print(a.combinationSum(candidates, target))
