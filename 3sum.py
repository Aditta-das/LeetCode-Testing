class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        if len(nums) < 3:
            return  []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                sumThree = a + nums[l] + nums[r]
                if sumThree > 0:
                    r -= 1
                elif sumThree < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

nums = [-1,0,1,2,-1,-4]
a = Solution()
print(a.threeSum(nums))