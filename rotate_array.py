# Medium
class Solution(object):
    def rotate(self, nums, k):
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = a[i]
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
a = Solution()
print(a.rotate(nums, k))