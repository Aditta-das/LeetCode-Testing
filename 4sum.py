class Solution(object):
    def fourSum(self, nums, target):
        if not nums and len(nums) < 4:
            return []
        
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):      
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue

                sumA = nums[i] + nums[j]
                l, r = j+1, len(nums)-1
                
                while l < r:
                    sumB = sumA + nums[l] + nums[r]
                    if sumB == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif sumB < target:
                        l += 1
                    else:
                        r -= 1
        return res               


nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9
a = Solution()
print(a.fourSum(nums, target))