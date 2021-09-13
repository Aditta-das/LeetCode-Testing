# Easy
class Solution(object):
    def sortedSquares(self, nums):
        res = [None] * len(nums)
        left, right = 0, len(nums)-1
        for idx in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[idx] = nums[left] ** 2
                left += 1
            else:
                res[idx] = nums[right] ** 2
                right -= 1
        return res

nums = [-4,-1,0,3,10]
a = Solution()
print(a.sortedSquares(nums))