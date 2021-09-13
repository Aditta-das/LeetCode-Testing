class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxi = 0
        while l < r:
            min_h = min(height[l], height[r])
            new_len = r - l
            max_val = min_h * new_len
            maxi = max(maxi, max_val)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxi



height = [4,3,2,1,4]
a = Solution()
print(a.maxArea(height))