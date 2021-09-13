class Solution(object):
    def moveZeroes(self, nums):
        s, c = -1, 0
        while c < len(nums):
            if not nums[c] == 0:
                s+=1
                nums[c], nums[s] = nums[s], nums[c]
            c += 1
        return nums



nums = [0,1,0,3,12]
a = Solution()
print(a.moveZeroes(nums))