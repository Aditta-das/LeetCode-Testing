class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else: 
                right -= 1


numbers = [2,3,4]
target = 6
a = Solution()
print(a.twoSum(numbers, target))